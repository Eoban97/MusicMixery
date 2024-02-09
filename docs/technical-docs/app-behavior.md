---
title: App-Verhalten
parent: Technische Dokumentation
nav_order: 3
---

{: .label }
Eoban Munsi, Wakman Safi, Ertan Tunc

# App-Verhalten
{: .no_toc }

Diese Seite bietet eine umfassende Beschreibung des Verhaltens unserer Anwendung, einschließlich Benutzerinteraktion, Datenverwaltung, Authentifizierung und Autorisierung, Fehlerbehandlung, Leistungsaspekten, Sicherheitsüberlegungen, Skalierbarkeit und Anpassungsfähigkeit.

<details open markdown="block">
{: .text-delta }
<summary>Inhaltsverzeichnis</summary>
+ ToC
{: toc }
</details>

## Benutzerinteraktion

Unsere Anwendung ermöglicht es Benutzern, sich zu registrieren, einzuloggen, nach Songs zu suchen, Playlists zu erstellen, Songs zu ihren Playlists hinzuzufügen oder zu entfernen und vieles mehr. Die Benutzerinteraktion ist intuitiv gestaltet und durch eine benutzerfreundliche Oberfläche erleichtert.

## Datenverwaltung

Das Datenmodell unserer Anwendung umfasst Entitäten wie Benutzer, Songs und Playlists. Diese werden in einer relationalen Datenbank verwaltet, wobei die Beziehungen zwischen den Entitäten definiert sind, um die erforderliche Funktionalität zu ermöglichen.

## Authentifizierung und Autorisierung

Benutzer können sich sicher registrieren und einloggen. Die Anwendung verfügt über Mechanismen zur Authentifizierung und Autorisierung, um sicherzustellen, dass nur autorisierte Benutzer auf bestimmte Funktionen zugreifen können.

## Fehlerbehandlung

Unsere Anwendung ist so konzipiert, dass sie robust und fehlertolerant ist. Fehler werden angemessen behandelt und dem Benutzer mit aussagekräftigen Fehlermeldungen angezeigt. Im Backend können durch Flask Erweiterungen unerwartete Fehler protokolliert und analysiert werden, um die Stabilität der Anwendung zu gewährleisten.

## Sicherheitsüberlegungen

Die Sicherheit unserer Benutzerdaten hat oberste Priorität. Passwörter werden sicher verschlüsselt und gespeichert, um die Vertraulichkeit der Benutzerinformationen zu gewährleisten. Zusätzlich haben wir die Passwortlänge definiert, um die Sicherheit der Passwörter zu erhöhen.

## Skalierbarkeit

Unsere Anwendung ist skalierbar und kann bei Bedarf problemlos erweitert werden. Neue Funktionen können einfach hinzugefügt und die vorhandene Infrastruktur erweitert werden, um mit steigender Benutzerzahl umzugehen, ohne dabei die Leistung oder Stabilität der Anwendung zu beeinträchtigen.

## Anpassungsfähigkeit und Flexibilität

Unsere Anwendung bietet den Benutzern die Möglichkeit, ihre eigenen Playlists zu erstellen und zu verwalten. Darüber hinaus gibt es Optionen für benutzerdefinierte Einstellungen und Vorlieben, um die Benutzererfahrung weiter anzupassen und zu personalisieren.

Diese Beschreibung bietet einen umfassenden Überblick über das Verhalten unserer Anwendung und vermittelt den Benutzern ein klares Verständnis davon, wie sie die Anwendung nutzen können und wie sie funktioniert.
