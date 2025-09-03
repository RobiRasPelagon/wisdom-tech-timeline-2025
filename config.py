# --- Configuration File for Wisdom Tech Timeline 2025 ---
# This file contains all the key parameters for the project.
# Edit these values to configure the AI's behavior, sensors, and missions.

# 1. AI Core Configuration
AI_NAME = "Stibera"  # Name of our ethical AI companion
LOG_LEVEL = "INFO"   # How much information to log (DEBUG, INFO, WARNING, ERROR)
HEARTBEAT_INTERVAL = 60  # Seconds between system health checks

# 2. Ethical Engine Parameters
# These are the core rules that the AI cannot violate.
# Detailed rules will be loaded from a separate ethics file.
ETHICS_CONFIG_PATH = "src/ethics_policy.yaml"
MAX_IMPACT_LEVEL = 0.01  # Maximum allowed environmental impact on a scale of 0 to 1
PRIORITY_DIRECTIVE = "PRESERVE_LIFE_AND_HARMONY"  # The ultimate guiding principle

# 3. Sensor Configuration
SENSORS_ENABLED = {
    "camera": True,
    "microphone": True,
    "gps": True,
    "temperature": True,
    "humidity": True,
    "air_quality": True,
    "soil_moisture": False, # Example of a sensor that is currently disabled
    "subtle_energy_detector": True # For detecting telluric currents and ley lines
}
CAMERA_RESOLUTION = (1920, 1080)
AUDIO_SAMPLE_RATE = 44100  # Hz

# 4. Hardware and Propulsion Systems Configuration
# For the Harmony-Class Research Cruiser
PROPULSION_SYSTEM = {
    "LEVITATION_ENGINE": {
        "TYPE": "Acoustic Resonance",
        "MIN_FREQ_HZ": 20,
        "MAX_FREQ_HZ": 200,
        "DEFAULT_HARMONIC": "Schumann Resonance 7.83Hz based"
    },
    "PLASMA_DRIVE": {
        "TYPE": "Hydrogen Plasma",
        "MAX_THRUST_PERCENT": 80
    },
    "PLASMA_STEALTH_LAYER": {
        "ENABLED": True,
        "MIN_SPEED_KPH_FOR_ACTIVATION": 1000
    }
}

# 5. Materials Science Database
# Paths to databases for our bio-composite research
BIOCOMPOSITE_RECIPES_DB = "data/biocomposites.json"
NATURAL_POLYMERS_DB = "data/natural_polymers.json"

# 6. Community and Data Sharing
# Where to upload the collected data from missions
PUBLIC_DATA_REPOSITORY_URL = "https://example.com/data-archive" # We will create this later
ALLOW_ANONYMOUS_CONTRIBUTIONS = True

# --- End of Configuration ---

