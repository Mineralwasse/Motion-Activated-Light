import os
import subprocess
import logging

# Konfiguration
GIT_PATH = r"C:\Program Files\Git\cmd\git.exe"
REPO_PATH = os.path.dirname(os.path.abspath(__file__))

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_for_updates():
    """Prüft, ob auf GitHub eine neue Version vorliegt."""
    try:
        env = os.environ.copy()
        # Fetch remote changes
        logger.info("Prüfe auf Updates (git fetch)...")
        subprocess.run([GIT_PATH, "fetch"], cwd=REPO_PATH, env=env, check=True, capture_output=True)
        
        # Status prüfen
        result = subprocess.run(
            [GIT_PATH, "status", "-uno"], 
            cwd=REPO_PATH, env=env, check=True, capture_output=True, text=True
        )
        
        if "Your branch is behind" in result.stdout:
            logger.info("Update verfügbar!")
            return True
        else:
            logger.info("Projekt ist auf dem neuesten Stand.")
            return False
            
    except Exception as e:
        logger.error(f"Fehler bei der Update-Prüfung: {e}")
        return False

def install_update():
    """Installiert das verfügbare Update."""
    try:
        env = os.environ.copy()
        logger.info("Installiere Update (git pull)...")
        result = subprocess.run(
            [GIT_PATH, "pull"], 
            cwd=REPO_PATH, env=env, check=True, capture_output=True, text=True
        )
        logger.info(f"Update-Ergebnis: {result.stdout}")
        return True
    except Exception as e:
        logger.error(f"Fehler bei der Update-Installation: {e}")
        return False

if __name__ == "__main__":
    if check_for_updates():
        # In einer echten App würde hier ein Button in der UI den install_update Aufruf triggern
        print("Ein Update ist verfügbar. Möchten Sie es installieren? (y/n)")
        # choice = input()
        # if choice.lower() == 'y':
        #     install_update()
        pass
