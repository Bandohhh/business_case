import sys
from pathlib import Path
# This tells pytest: “treat the repo root as a place to import from”
# Add the project root to Python path so "import src" works
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
