---
title: App Structure
parent: Technical Docs
nav_order: 1
---

{: .label }
Eoban Munsi, Wakman Safi, Ertan Tunc

# [App structure, incl. context]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

![get_list_todos_sample](assets/images/app_structure_MusicMixery.png)

## MUSICMIXERY-MAIN

### Docs Folder

Hier werden die Seiten definiert und mit Inhalt gefüllt, die zur Generierung der GitHub-Page genutzt werden.

### Instance

Lokale Datenbank, die von app.py und script.py genutzt und befüllt wird.

### Templates

Enthält HTML-Codes für das Frontend-Design der verschiedenen Seiten. Die base.html implementiert vorgefertigte Designbausteine, von denen andere HTML-Seiten erben.

### venv

Beinhaltet alle Installationen und Dateien, die benötigt werden, um den Rahmen der Webapplikation zu geben und sie ausführbar zu machen.

## app.py

Die Anwendungslogik wird hier definiert. Es handelt sich um eine Flask-Anwendung, die verschiedene Routen und Formulare für die Benutzerinteraktion implementiert. Es enthält auch die Definitionen für das Datenmodell der Anwendung, das über SQLAlchemy mit einer SQLite-Datenbank verbunden ist. Die Hauptmerkmale von app.py sind:

- Flask-Setup
- Datenmodell
- Formulare
- Routen
- Authentifizierung und Autorisierung
- Datenbankinteraktion
- Fehlerbehandlung
- Hauptseite

## README.md

Anleitung zur korrekten Ausführung der Applikation.

## Requirements.txt

Generierte Datei, die die erforderlichen Software-Anwendungen und deren Versionen für die Ausführung der Applikation enthält.

## script.py

Beinhaltet Testdaten und die Funktion zum Einfügen in die Datenbank.
