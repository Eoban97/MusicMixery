from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError, Optional
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret'  # adjust this later

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(820), nullable=False)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    takt = db.Column(db.String(20), nullable=False)
    tempo = db.Column(db.Integer, nullable=False)
    tonart = db.Column(db.String(50), nullable=False)


playlist_songs = db.Table('playlist_songs',
                          db.Column('playlist_id',
                                    db.Integer, db.ForeignKey('playlist.id'),
                                    primary_key=True),
                          db.Column('song_id',
                                    db.Integer,
                                    db.ForeignKey('song.id'),
                                    primary_key=True))


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('playlists', lazy=True))
    songs = db.relationship('Song', secondary=playlist_songs, lazy='subquery',
                            backref=db.backref('playlists', lazy=True))


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)],
                             render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("username already exists")


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)],
                             render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


class SearchForm(FlaskForm):
    name = StringField('Name', validators=[Optional()])
    artist_name = StringField('Artist Name', validators=[Optional()])
    tonart = SelectField('Tonart', validators=[Optional()])
    genre = SelectField('Genre', validators=[Optional()])
    takt = SelectField('Takt', validators=[Optional()])
    release_start = DateField('Release Start', validators=[Optional()])
    release_end = DateField('Release End', validators=[Optional()])
    tempo_min = IntegerField('Tempo Min', validators=[Optional()])
    tempo_max = IntegerField('Tempo Max', validators=[Optional()])
    submit = SubmitField('Search')


class CreatePlaylistForm(FlaskForm):
    name = StringField('Playlist Name', validators=[InputRequired(),
                                                    Length(min=1, max=40)])
    submit = SubmitField('Create')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Wrong username or password')

    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    form.tonart.choices = [('', 'any')] + [(t.tonart, t.tonart) for t
                                           in Song.query.with_entities(
                                               Song.tonart
                                               ).distinct()]
    form.genre.choices = [('', 'any')] + [(g.genre, g.genre) for g
                                          in Song.query.with_entities(
                                              Song.genre
                                              ).distinct()]
    form.takt.choices = [('', 'any')] + [(t.takt, t.takt) for t
                                         in Song.query.with_entities(
                                             Song.takt
                                             ).distinct()]

    songs = []
    if form.validate_on_submit():
        query = Song.query
        if form.name.data:
            query = query.filter(Song.title.ilike(f'%{form.name.data}%'))
        if form.artist_name.data:
            query = query.filter(Song.artist_name.ilike(
                f'%{form.artist_name.data}%'))
        if form.tonart.data:
            query = query.filter(
                    Song.tonart ==
                    form.tonart.data) if form.tonart.data != 'any' else query
        if form.genre.data:
            query = query.filter(
                    Song.genre ==
                    form.genre.data) if form.genre.data != 'any' else query
        if form.takt.data:
            query = query.filter(
                    Song.takt ==
                    form.takt.data) if form.takt.data != 'any' else query
        if form.release_start.data:
            query = query.filter(Song.release_date >= form.release_start.data)
        if form.release_end.data:
            query = query.filter(Song.release_date <= form.release_end.data)
        if form.tempo_min.data:
            query = query.filter(Song.tempo >= form.tempo_min.data)
        if form.tempo_max.data:
            query = query.filter(Song.tempo <= form.tempo_max.data)

        songs = query.all()
    return render_template('search.html', form=form, songs=songs)


@app.route('/playlists', methods=['GET', 'POST'])
@login_required
def playlists():
    form = CreatePlaylistForm()
    if form.validate_on_submit():
        new_playlist = Playlist(name=form.name.data, user_id=current_user.id)
        db.session.add(new_playlist)
        db.session.commit()
        return redirect(url_for('playlists'))

    user_playlists = Playlist.query.filter_by(user_id=current_user.id).all()
    return render_template('playlists.html', form=form,
                           playlists=user_playlists)


@app.route('/playlists/<int:playlist_id>', methods=['GET', 'POST'])
@login_required
def playlist(playlist_id):
    playlist = Playlist.query.filter_by(id=playlist_id, user_id=current_user.id
                                        ).first()
    if playlist:
        songs = playlist.songs
        return render_template('playlist.html', playlist=playlist, songs=songs)

    return render_template('notfound.html')


@app.route('/add_song_to_playlist/<int:song_id>', methods=['POST'])
@login_required
def add_song_to_playlist(song_id):
    playlist_id = request.form.get('playlist_id')
    if playlist_id:
        playlist = Playlist.query.filter_by(id=playlist_id,
                                            user_id=current_user.id).first()
        if playlist:
            existing_song = next((song for song in playlist.songs
                                  if song.id == song_id), None)
            if not existing_song:
                song = Song.query.get(song_id)
                if song:
                    playlist.songs.append(song)
                    db.session.commit()
                    return jsonify('Song added to playlist successfully.'), 200
                else:
                    return jsonify('Song not found.'), 404
            else:
                return jsonify('Song already in playlist.'), 400
        else:
            return jsonify('Playlist not found.'), 404
    else:
        return jsonify('No playlist selected.', 400)

    return redirect(url_for('search'))


@app.route('/delete_playlist/<int:playlist_id>', methods=['POST'])
@login_required
def delete_playlist(playlist_id):
    playlist = Playlist.query.filter_by(id=playlist_id,
                                        user_id=current_user.id).first()
    if playlist:
        db.session.delete(playlist)
        db.session.commit()
    else:
        flash('Playlist not found or you do not have permission to delete it.',
              'error')
    return redirect(url_for('playlists'))


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=6020)
