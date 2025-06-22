# TeamCampus Schulplattform

Dies ist ein einfaches Beispiel einer Schulplattform namens **TeamCampus**.
Die Anwendung basiert auf [Flask](https://flask.palletsprojects.com/) und bietet
folgende Funktionen:

- Registrierung und Login von Benutzern
- Erstellen von Teams und Hinzufügen von Kursen zu Teams
- Abrufen von Teams und Kursen über eine einfache REST-Schnittstelle

## Installation

1. Python 3.12 oder neuer installieren.
2. Benötigte Abhängigkeiten installieren:
   ```bash
   pip install Flask
   ```

## Nutzung

Die Anwendung befindet sich in `teamcampus/app.py`. Starten Sie den Server mit:

```bash
python3 teamcampus/app.py
```

Anschließend stehen folgende Endpunkte zur Verfügung (Beispiele nutzen `curl`):

- **Registrierung**
  ```bash
  curl -X POST -H "Content-Type: application/json" \
       -d '{"username": "max", "password": "geheim"}' \
       http://localhost:5000/register
  ```
- **Login**
  ```bash
  curl -X POST -H "Content-Type: application/json" \
       -d '{"username": "max", "password": "geheim"}' \
       http://localhost:5000/login
  ```
- **Team anlegen**
  ```bash
  curl -X POST -H "Content-Type: application/json" \
       -d '{"name": "Mathe-Team"}' \
       http://localhost:5000/teams
  ```
- **Kurs zu Team hinzufügen**
  ```bash
  curl -X POST -H "Content-Type: application/json" \
       -d '{"course": "Algebra"}' \
       http://localhost:5000/team/Mathe-Team/courses
  ```
- **Alle Teams auflisten**
  ```bash
  curl http://localhost:5000/teams
  ```

Diese Plattform ist nur als Beispiel gedacht und nutzt keinen persistenten
Speicher. Für eine produktive Nutzung sollten Datenbank, Authentifizierung und
Sicherheit erweitert werden.
