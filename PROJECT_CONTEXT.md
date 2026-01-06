# PROJECT_CONTEXT - Motion Activated Light

## Zweck des Projekts
Dieses Projekt enthält ein Home Assistant Blueprint für eine bewegungs- und türkontaktgesteuerte Lichtsteuerung. Es ermöglicht das automatische Einschalten eines Schalters oder Lichts, wenn Bewegung erkannt oder eine Tür geöffnet wird, mit konfigurierbarer Ausschaltverzögerung und maximaler Einschaltdauer.

## Architektur
- **Blueprint-basiert:** Nutze YAML-Konfigurationen für Home Assistant.
- **Trigger:** Reagiert auf Zustandsänderungen (`on`/`off`) von Binärsensoren (Bewegung, Tür).
- **Logik:** 
  - Einschalten bei Aktivität.
  - Ausschalten nach Verzögerung (`delay_off`) ohne Aktivität.
  - Sicherheitsabschaltung nach maximaler Dauer (`max_on_duration`), optional mit Berücksichtigung aktiver Sensoren.

## Wichtige Abhängigkeiten
- Home Assistant (Version mit Blueprint-Unterstützung)
- Git für Versionierung und Updates

## Besonderheiten
- Unterstützung für mehrere Bewegungs- und Türkontaktsensoren.
- Restart-Modus für sofortige Reaktion auf neue Ereignisse während Verzögerungszeiten.
- Update-Prüfung über GitHub (in Planung/Integration).

## Offene Punkte
- [ ] Vollständige GitHub-Integration mit Updater-Skript.
- [ ] Erstellung der `setup_git.bat`.
- [ ] Dokumentation der Installationsschritte für Endnutzer.
