---
title: Referenz
parent: Technische Dokumentation
nav_order: 4
---

{: .label }
[Eoban Munsi, Wakman Safi, Ertan Tunc]

# [Referenzdokumentation]
{: .no_toc }


<details open markdown="block">
{: .text-delta }
<summary>Inhaltsverzeichnis</summary>
+ Inhalt
{: toc }
</details>

## Route: `/register`

### `register()`

**Methoden:** `GET` `POST`

**Zweck:** Zeigt das Registrierungsformular an und verarbeitet Registrierungsanfragen. Benutzer können sich registrieren, indem sie einen Benutzernamen und ein Passwort eingeben.

---

## Route: `/login`

### `login()`

**Methoden:** `GET` `POST`

**Zweck:** Zeigt das Anmeldeformular an und verarbeitet Anmeldeanfragen. Benutzer können sich anmelden, indem sie ihren Benutzernamen und ihr Passwort eingeben.

---

## Route: `/logout`

### `logout()`

**Methoden:** `GET` `POST`

**Zweck:** Meldet den Benutzer ab und leitet ihn zur Anmeldeseite weiter.

---

## Route: `/search`

### `search()`

**Methoden:** `GET` `POST`

**Zweck:** Ermöglicht angemeldeten Benutzern die Suche nach Songs. Das Suchformular ermöglicht die Filterung nach verschiedenen Kriterien wie Songtitel, Künstlername, Tonart, Genre, Veröffentlichungsdatum und Tempo.

---

## Route: `/playlists`

### `playlists()`

**Methoden:** `GET` `POST`

**Zweck:** Zeigt die Playlists des angemeldeten Benutzers an und ermöglicht es ihm, neue Playlists zu erstellen.

---

## Route: `/playlists/<int:playlist_id>`

### `playlist(playlist_id)`

**Methoden:** `GET` `POST`

**Zweck:** Zeigt die Details einer bestimmten Playlist an, einschließlich der enthaltenen Songs.

---

## Route: `/add_song_to_playlist/<int:song_id>`

### `add_song_to_playlist(song_id)`

**Methoden:** `POST`

**Zweck:** Fügt einen bestimmten Song zur ausgewählten Playlist des angemeldeten Benutzers hinzu.

---

## Route: `/delete_playlist/<int:playlist_id>`

### `delete_playlist(playlist_id)`

**Methoden:** `GET` `POST`

**Zweck:** Löscht eine bestimmte Playlist des angemeldeten Benutzers.

---

## Route: `/delete_song_from_playlist/<int:playlist_id>/<int:song_id>`

### `delete_song_from_playlist(playlist_id, song_id)`

**Methoden:** `GET` `POST`

**Zweck:** Entfernt einen bestimmten Song aus einer bestimmten Playlist des angemeldeten Benutzers.

---

## Route: `/`

### `home()`

**Methoden:** `GET`

**Zweck:** Die Startseite der Anwendung, die nach erfolgreicher Anmeldung angezeigt wird.
