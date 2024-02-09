---
title: Data Model
parent: Technical Docs
nav_order: 3
---

{: .label }
Eoban Munsi, Wakman Safi, Ertan Tunc

# Data model
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Allgemein

Unser Datenmodell definiert die Struktur und die Beziehungen zwischen Nutzern.
In unserer script.py haben wir die Testdaten, sowie die Funktion zur einbindung in die Datenbank geschrieben. Die Testdaten wurden automatisch zufällig mit https://www.mockaroo.com/ erstellt.

## User

### `User`

**id**: Eindeutige Kennung für jeden Benutzer.

**username**: Der Benutzername des Benutzers. Muss eindeutig sein und kann nicht NULL sein.

**password**: Das verschlüsselte Passwort des Benutzers. Kann nicht NULL sein.

## Song

### `Song`

**id**: Eindeutige Kennung für jeden Song.

**artist_name**: Der Name des Künstlers oder der Band, der den Song erstellt hat. Kann nicht NULL sein.

**title**: Der Titel des Songs. Kann nicht NULL sein.

**release_date**: Das Veröffentlichungsdatum des Songs.

**duration**: Die Dauer des Songs in Sekunden.

**genre**: Das Genre des Songs.

**takt**: Der Takt des Songs (z.B. 4/4).

**tempo**: Das Tempo des Songs in BPM (Beats Per Minute).

**tonart**: Die Tonart des Songs.

## Playlist

### `Playlist`

**id**: Eindeutige Kennung für jede Playlist.

**name**: Der Name der Playlist. Kann nicht NULL sein.

**user_id**: Die ID des Benutzers, dem die Playlist gehört.

**user**: Eine Beziehung zum Benutzer, der die Playlist erstellt hat.

**songs**: Eine dynamische Beziehung zu den Songs, die in der Playlist enthalten sind. Es handelt sich um eine Many-to-Many-Beziehung, die durch die `playlist_songs`-Tabelle vermittelt wird.

## playlist_songs

**playlist_id**: Die ID der Playlist in der Beziehung zur `Playlist`-Tabelle.

**song_id**: Die ID des Songs in der Beziehung zur `Song`-Tabelle.

Diese Tabelle dient als Zwischentabelle, um die Many-to-Many-Beziehung zwischen Playlists und Songs zu ermöglichen.
