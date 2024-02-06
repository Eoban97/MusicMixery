from app import Song, db
from datetime import datetime


def insert_songs(data):
    for song_data in data:
        song = Song(
            artist_name=song_data["artist_name"],
            title=song_data["title"],
            release_date=datetime.strptime(song_data["release_date"], "%Y-%m-%d").date(),
            duration=song_data["duration"],
            genre=song_data["genre_style"],
            takt=song_data.get("takt"),
            tempo=song_data.get("tempo"),
            tonart=song_data.get("tonart")
        )
        db.session.add(song)
    db.session.commit()
