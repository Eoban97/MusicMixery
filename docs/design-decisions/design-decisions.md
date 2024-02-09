---
title: Design Decisions
nav_order: 3
---

{: .label }
Eoban Munsi, Wakman Safi, Ertan Tunc

# [Design decisions]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Webdesign

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 01-Jan-2024

### Problem statement

Frontend: Wie schaffen wir eine angenehmes Nutzererlebnis

### Decision

Wir haben uns gemeinsam dazu entschieden ein simples Design zu nehmen , die nutzbaren Buttons und Möglichkeiten der App sind auf ein minimum reduziert, um für unseren Use-Case das bestmögliche Erlebnis zu schaffen, ohne große Ablenkung und Konzentration auf die wesentlichen Funktionalitäten

## 02: Datenbankdesign

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 15-Jan-2024

### Problem Statement

Datenbank: Welche Tables sind zu erstellen und welche Parameter wurden genutzt

### Decision

1. **Tabellenstruktur**

   - Es wurden drei Haupttabellen erstellt: User, Song und Playlist, um Benutzerinformationen, Songdaten und Playlists zu speichern.
   
2. **Parameterauswahl**

   - Für die User-Tabelle wurden Benutzername und Passwort als wesentliche Parameter ausgewählt, um die Benutzeranmeldung zu ermöglichen.
   - In der Song-Tabelle wurden Parameter wie Künstlername, Titel, Veröffentlichungsdatum, Dauer, Genre, Takt, Tempo und Tonart ausgewählt, um alle relevanten Informationen zu einem Song zu speichern.
   - Die Playlist-Tabelle enthält Parameter wie Namen und Benutzer-ID, um Benutzer-spezifische Playlists zu verwalten.

Die Entscheidung für diese Tabellenstruktur und Parameterauswahl wurde getroffen, um eine effiziente Speicherung und Verwaltung von Benutzer-, Song- und Playlistdaten in der Datenbank zu ermöglichen.

## 03: Datenbankinteraktion

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 19-Jan-2024

### Problem Statement

Datenbank: Welche Bibliothek nutzen wir zur Interaktion mit der Datenbank

### Decision

1. **Verwendung von SQLAlchemy**

   Wir haben uns für SQLAlchemy entschieden, weil es eine benutzerfreundliche Schnittstelle und ORM-Funktionen bietet, die die Datenbankmodellierung und -interaktion vereinfachen. Zudem ermöglicht es eine objektorientierte Herangehensweise an die Datenbank, was die Entwicklung erleichtert und den Code lesbarer macht. SQLAlchemy ist in der Python-Community weit verbreitet und bietet eine aktive Unterstützung sowie eine große Entwicklerbasis. Es bietet auch Flexibilität und Skalierbarkeit für zukünftige Erweiterungen und Änderungen in der Anwendung.

### Regarded Option

1. **Natives SQL-Querying**

   - Pro: Direktes SQL-Querying bietet maximale Kontrolle über die Datenbankinteraktion und kann in einigen Fällen effizienter sein.
   - Con: Es erfordert detailliertes Wissen über SQL und kann zu komplexem Code führen, der schwer zu warten ist.

2. **ORM-Frameworks anderer Sprachen**

   - Pro: Es gibt alternative ORM-Frameworks in anderen Sprachen wie Django ORM für Python.
   - Con: es bietet nicht immer die gleiche Flexibilität wie SQLAlchemy.


## 04: Struktureller Aufbau des Repositories

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 25-Jan-2024

### Problem Statement

In welcher Struktur schreiben wir unsere Anwendung

### Decision

Wir haben uns dazu entschieden, die Klassen in der app.py Datei zu schreiben. Die Anwendungsstruktur wurde organisiert, um Formulare, Datenbankmodelle und Routen in separate Dateien zu trennen, was die Wartung und Skalierbarkeit der Anwendung erleichtert.

### Regarded Option

1. **Kleinere Aufteilung**

   - Pro: man kann einzelne Bausteine einfacher zu Ordnen
   - Con: es kann schnell zur Unordnung kommen und wirkt wenig übersichtlich


