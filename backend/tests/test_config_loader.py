import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND_DIR))

from core.config_loader import ConfigLoader

loader = ConfigLoader()

print("=" * 60)
print("Testing Config Loader")
print("=" * 60)

print()

print("ICP Configuration")
print(loader.get_icp())

print()

print("Personas Configuration")
print(loader.get_personas())

print()

print("Triggers Configuration")
print(loader.get_triggers())

print()

print("Providers Configuration")
print(loader.get_providers())

print()

print("=" * 60)
print("Config Loader Test Passed")
print("=" * 60)
