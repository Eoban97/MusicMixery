from app import Song, db
from datetime import datetime

data = {
  "artist_name": "Prent Chadwell",
  "title": "viverra eget congue eget",
  "release_date": "2004-06-03",
  "duration": 454,
  "genre_style": "Opera",
  "takt": "2/2",
  "tempo": 69,
  "tonart": "G major"
}, {
  "artist_name": "Isabelle Padula",
  "title": "tortor sollicitudin",
  "release_date": "1966-10-02",
  "duration": 179,
  "genre_style": "Funk",
  "takt": "6/8",
  "tempo": 78,
  "tonart": "D minor"
}, {
  "artist_name": "Jean Maiden",
  "title": "hac habitasse platea dictumst maecenas",
  "release_date": "1970-06-26",
  "duration": 429,
  "genre_style": "Pop",
  "takt": "6/4",
  "tempo": 112,
  "tonart": "G major"
}, {
  "artist_name": "Lenora Rawe",
  "title": "phasellus sit amet",
  "release_date": "1937-05-17",
  "duration": 56,
  "genre_style": "Latin",
  "takt": "2/2",
  "tempo": 99,
  "tonart": "G major"
}, {
  "artist_name": "Violette Stother",
  "title": "sit",
  "release_date": "1986-05-23",
  "duration": 98,
  "genre_style": "Disco",
  "takt": "4/8",
  "tempo": 102,
  "tonart": "D minor"
}, {
  "artist_name": "Devon McCurt",
  "title": "molestie",
  "release_date": "1912-07-14",
  "duration": 377,
  "genre_style": "Rock",
  "takt": "4/8",
  "tempo": 84,
  "tonart": "G major"
}, {
  "artist_name": "De witt Byrth",
  "title": "nec nisi",
  "release_date": "1933-03-02",
  "duration": 125,
  "genre_style": "Opera",
  "takt": "6/4",
  "tempo": 99,
  "tonart": "G major"
}, {
  "artist_name": "Geoffrey Daburn",
  "title": "libero non mattis pulvinar nulla pede",
  "release_date": "1916-12-14",
  "duration": 188,
  "genre_style": "Gospel",
  "takt": "3/4",
  "tempo": 108,
  "tonart": "G major"
}, {
  "artist_name": "Debera Mandrake",
  "title": "ut nulla sed accumsan felis ut",
  "release_date": "2024-02-02",
  "duration": 327,
  "genre_style": "Opera",
  "takt": "5/4",
  "tempo": 99,
  "tonart": "D minor"
}, {
  "artist_name": "Eugene Smead",
  "title": "sem",
  "release_date": "1930-03-13",
  "duration": 471,
  "genre_style": "Techno",
  "takt": "6/4",
  "tempo": 41,
  "tonart": "D minor"
}, {
  "artist_name": "Krysta McGeachy",
  "title": "duis bibendum morbi",
  "release_date": "1904-12-27",
  "duration": 21,
  "genre_style": "Latin",
  "takt": "6/4",
  "tempo": 97,
  "tonart": "G major"
}, {
  "artist_name": "Danell Leyland",
  "title": "justo lacinia eget tincidunt eget tempus vel",
  "release_date": "1968-10-05",
  "duration": 209,
  "genre_style": "Gospel",
  "takt": "3/8",
  "tempo": 65,
  "tonart": "C major"
}, {
  "artist_name": "Peter Vedntyev",
  "title": "quis",
  "release_date": "2013-05-11",
  "duration": 162,
  "genre_style": "House",
  "takt": "3/2",
  "tempo": 49,
  "tonart": "D minor"
}, {
  "artist_name": "Cara Satterley",
  "title": "lectus in est risus auctor",
  "release_date": "1917-03-29",
  "duration": 72,
  "genre_style": "EDM",
  "takt": "6/4",
  "tempo": 71,
  "tonart": "C major"
}, {
  "artist_name": "Patrizia Asp",
  "title": "cras mi pede malesuada in",
  "release_date": "1925-12-22",
  "duration": 129,
  "genre_style": "Reggae",
  "takt": "2/4",
  "tempo": 101,
  "tonart": "D minor"
}, {
  "artist_name": "Dun Rolinson",
  "title": "mollis molestie lorem quisque",
  "release_date": "1930-02-07",
  "duration": 358,
  "genre_style": "Funk",
  "takt": "2/2",
  "tempo": 58,
  "tonart": "G major"
}, {
  "artist_name": "Aloisia Bloor",
  "title": "sit amet",
  "release_date": "1901-12-22",
  "duration": 250,
  "genre_style": "Jazz",
  "takt": "3/8",
  "tempo": 58,
  "tonart": "C major"
}, {
  "artist_name": "Abramo Idney",
  "title": "justo eu massa donec dapibus duis",
  "release_date": "1945-09-19",
  "duration": 115,
  "genre_style": "House",
  "takt": "4/4",
  "tempo": 41,
  "tonart": "C major"
}, {
  "artist_name": "Fayth Halford",
  "title": "eleifend pede libero quis orci nullam molestie",
  "release_date": "1954-02-07",
  "duration": 178,
  "genre_style": "Afrobeat",
  "takt": "5/4",
  "tempo": 105,
  "tonart": "D minor"
}, {
  "artist_name": "Beckie Weighell",
  "title": "quis libero nullam",
  "release_date": "1927-06-22",
  "duration": 265,
  "genre_style": "Blues",
  "takt": "3/2",
  "tempo": 52,
  "tonart": "C major"
}, {
  "artist_name": "Charyl Crowley",
  "title": "praesent lectus vestibulum quam",
  "release_date": "1903-06-20",
  "duration": 183,
  "genre_style": "Grunge",
  "takt": "5/4",
  "tempo": 41,
  "tonart": "C major"
}, {
  "artist_name": "Nichole Hember",
  "title": "luctus ultricies",
  "release_date": "2010-01-18",
  "duration": 35,
  "genre_style": "Rock",
  "takt": "3/8",
  "tempo": 69,
  "tonart": "G major"
}, {
  "artist_name": "Cammi Biddwell",
  "title": "felis",
  "release_date": "1902-01-12",
  "duration": 384,
  "genre_style": "Ambient",
  "takt": "6/8",
  "tempo": 107,
  "tonart": "C major"
}, {
  "artist_name": "Romain Bryde",
  "title": "viverra diam vitae",
  "release_date": "1983-12-12",
  "duration": 258,
  "genre_style": "Techno",
  "takt": "3/8",
  "tempo": 99,
  "tonart": "D minor"
}, {
  "artist_name": "Stacy Bidgod",
  "title": "metus",
  "release_date": "1923-03-30",
  "duration": 27,
  "genre_style": "Techno",
  "takt": "3/4",
  "tempo": 43,
  "tonart": "D minor"
}, {
  "artist_name": "Buck Olivera",
  "title": "ut rhoncus",
  "release_date": "1914-01-20",
  "duration": 166,
  "genre_style": "Classical",
  "takt": "6/4",
  "tempo": 55,
  "tonart": "G major"
}, {
  "artist_name": "Lance Flewin",
  "title": "platea dictumst etiam faucibus cursus urna",
  "release_date": "1913-06-18",
  "duration": 91,
  "genre_style": "Reggaeton",
  "takt": "5/4",
  "tempo": 115,
  "tonart": "G major"
}, {
  "artist_name": "Gilda Lofthouse",
  "title": "sit amet consectetuer adipiscing elit proin risus",
  "release_date": "1902-02-23",
  "duration": 35,
  "genre_style": "Ambient",
  "takt": "4/4",
  "tempo": 83,
  "tonart": "D minor"
}, {
  "artist_name": "Simeon Dell Casa",
  "title": "erat quisque erat",
  "release_date": "1907-05-27",
  "duration": 74,
  "genre_style": "Techno",
  "takt": "6/8",
  "tempo": 77,
  "tonart": "D minor"
}, {
  "artist_name": "Nichole Dran",
  "title": "et magnis dis",
  "release_date": "1917-04-02",
  "duration": 484,
  "genre_style": "Indie",
  "takt": "3/4",
  "tempo": 70,
  "tonart": "C major"
}, {
  "artist_name": "Ysabel Revan",
  "title": "eu nibh quisque",
  "release_date": "1906-07-29",
  "duration": 421,
  "genre_style": "Afrobeat",
  "takt": "2/2",
  "tempo": 100,
  "tonart": "G major"
}, {
  "artist_name": "Wildon Tranfield",
  "title": "diam",
  "release_date": "2007-11-23",
  "duration": 307,
  "genre_style": "Funk",
  "takt": "3/8",
  "tempo": 72,
  "tonart": "D minor"
}, {
  "artist_name": "Valeria Ellicock",
  "title": "ipsum aliquam non mauris morbi",
  "release_date": "1995-02-27",
  "duration": 497,
  "genre_style": "Funk",
  "takt": "6/8",
  "tempo": 45,
  "tonart": "C major"
}, {
  "artist_name": "Lamar Bambrough",
  "title": "mollis molestie lorem",
  "release_date": "1967-09-28",
  "duration": 486,
  "genre_style": "Folk",
  "takt": "4/8",
  "tempo": 115,
  "tonart": "D minor"
}, {
  "artist_name": "Armando Puleque",
  "title": "lectus in quam fringilla rhoncus mauris",
  "release_date": "1933-08-12",
  "duration": 394,
  "genre_style": "Folk",
  "takt": "6/4",
  "tempo": 116,
  "tonart": "D minor"
}, {
  "artist_name": "Jaye Hebborne",
  "title": "cras",
  "release_date": "1966-06-02",
  "duration": 81,
  "genre_style": "Soul",
  "takt": "6/4",
  "tempo": 56,
  "tonart": "G major"
}, {
  "artist_name": "Doralynne Locke",
  "title": "integer",
  "release_date": "1956-06-28",
  "duration": 71,
  "genre_style": "Grunge",
  "takt": "3/2",
  "tempo": 43,
  "tonart": "C major"
}, {
  "artist_name": "Leigha McNutt",
  "title": "id",
  "release_date": "1974-06-11",
  "duration": 332,
  "genre_style": "K-pop",
  "takt": "3/4",
  "tempo": 46,
  "tonart": "G major"
}, {
  "artist_name": "Brinna Moulster",
  "title": "viverra eget congue eget semper rutrum nulla",
  "release_date": "1979-02-17",
  "duration": 130,
  "genre_style": "House",
  "takt": "4/4",
  "tempo": 104,
  "tonart": "D minor"
}, {
  "artist_name": "Marielle Rosenfelt",
  "title": "adipiscing molestie hendrerit at vulputate",
  "release_date": "1987-03-18",
  "duration": 326,
  "genre_style": "Folk",
  "takt": "3/4",
  "tempo": 78,
  "tonart": "D minor"
}, {
  "artist_name": "Randy Samwell",
  "title": "nisi venenatis tristique fusce",
  "release_date": "1972-06-18",
  "duration": 314,
  "genre_style": "Afrobeat",
  "takt": "3/4",
  "tempo": 85,
  "tonart": "G major"
}, {
  "artist_name": "Ardelis Sinson",
  "title": "eget rutrum at lorem integer",
  "release_date": "1926-08-31",
  "duration": 151,
  "genre_style": "Techno",
  "takt": "3/8",
  "tempo": 113,
  "tonart": "D minor"
}, {
  "artist_name": "Adore Neame",
  "title": "imperdiet",
  "release_date": "1921-10-14",
  "duration": 112,
  "genre_style": "Afrobeat",
  "takt": "2/4",
  "tempo": 80,
  "tonart": "G major"
}, {
  "artist_name": "Catherine Pudney",
  "title": "nam tristique",
  "release_date": "1975-07-02",
  "duration": 182,
  "genre_style": "Rock",
  "takt": "4/4",
  "tempo": 102,
  "tonart": "G major"
}, {
  "artist_name": "Myrtia Allderidge",
  "title": "congue",
  "release_date": "1952-10-16",
  "duration": 194,
  "genre_style": "Pop",
  "takt": "3/8",
  "tempo": 63,
  "tonart": "D minor"
}, {
  "artist_name": "Killian Attenburrow",
  "title": "habitasse platea dictumst aliquam augue",
  "release_date": "1970-03-24",
  "duration": 269,
  "genre_style": "Jazz",
  "takt": "2/2",
  "tempo": 56,
  "tonart": "G major"
}, {
  "artist_name": "Ashleigh Dunkley",
  "title": "duis",
  "release_date": "1997-08-12",
  "duration": 277,
  "genre_style": "Trance",
  "takt": "4/8",
  "tempo": 81,
  "tonart": "D minor"
}, {
  "artist_name": "Tallie Hillborne",
  "title": "fusce posuere felis sed lacus morbi sem",
  "release_date": "1949-12-02",
  "duration": 354,
  "genre_style": "Jazz",
  "takt": "6/4",
  "tempo": 47,
  "tonart": "G major"
}, {
  "artist_name": "Gerrie Creaser",
  "title": "sed vestibulum sit amet",
  "release_date": "1962-04-06",
  "duration": 28,
  "genre_style": "Disco",
  "takt": "6/4",
  "tempo": 85,
  "tonart": "C major"
}, {
  "artist_name": "Radcliffe Rockey",
  "title": "mauris",
  "release_date": "2022-10-07",
  "duration": 451,
  "genre_style": "Ska",
  "takt": "3/4",
  "tempo": 104,
  "tonart": "G major"
}

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
