# MusicMixery
Your favourite App to find new Music

## Setup
Clone the repo

### setup venv
```bash
virtualenv venv
source venv/bin/activate  for Unix/MacOS
venv\Scripts\activate     for Windows
pip install -r requirements.txt
```

### prepare the app
run:
```bash
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> from script import insert_songs, data
    >>> insert_songs(data)
    >>> exit() // or press ctrl+d
```
### run the app
```bash
python app.py
open localhost:6020 in your browser
```
