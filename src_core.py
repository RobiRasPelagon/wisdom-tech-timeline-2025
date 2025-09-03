# --- Core Components for the "Stibera" AI ---
# This file defines the main classes that form the AI's consciousness and operational logic.

import logging
import time
import yaml
import random

# Import configuration (we assume config.py is in the parent directory for now)
try:
    import config
except ImportError:
    print("Warning: config.py not found. Using default values.")
    # Define a fallback config object if config.py is not found
    class DefaultConfig:
        AI_NAME = "Stibera (Default)"
        ETHICS_CONFIG_PATH = "src/ethics_policy.yaml"
        SENSORS_ENABLED = {"camera": True, "microphone": True, "temperature": True}
    config = DefaultConfig()


class EthicsEngine:
    """
    The heart of the AI. It loads and enforces the ethical rules.
    Every major decision must be approved by this engine.
    """
    def __init__(self, policy_path):
        self.policy_path = policy_path
        self.rules = self._load_rules()
        logging.info("Ethics Engine initialized with policy: %s", self.policy_path)
        if not self.rules:
            logging.error("CRITICAL: Ethical policy could not be loaded. AI will operate in safe mode.")

    def _load_rules(self):
        try:
            with open(self.policy_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return None

    def is_action_allowed(self, action, context=None):
        """Checks if a proposed action is ethically permissible."""
        if not self.rules:
            return False  # Fail-safe: if no rules, no action is allowed

        primary_directive = self.rules.get('primary_directive', 'DO_NO_HARM')
        if primary_directive != "PRESERVE_LIFE_AND_HARMONY":
             logging.warning("Primary directive is not set to PRESERVE_LIFE_AND_HARMONY.")

        # Simple check for now: all actions are allowed if the rules are loaded
        # In the future, we will have detailed logic here.
        logging.info(f"[ETHICS CHECK] Action '{action}' is permitted.")
        return True


class SensorHub:
    """
    Manages all physical and virtual sensors.
    It simulates sensor readings for now.
    """
    def __init__(self):
        self.enabled_sensors = config.SENSORS_ENABLED
        logging.info("Sensor Hub initialized. Enabled sensors: %s", list(self.enabled_sensors.keys()))

    def read_all_sensors(self):
        """Returns a dictionary of readings from all enabled sensors."""
        data = {}
        if self.enabled_sensors.get("temperature"):
            data["temperature_celsius"] = round(random.uniform(15.0, 25.0), 2)
        if self.enabled_sensors.get("humidity"):
            data["humidity_percent"] = round(random.uniform(40.0, 60.0), 2)
        if self.enabled_sensors.get("air_quality"):
            data["air_quality_index"] = round(random.uniform(10.0, 40.0), 2)
        
        logging.info("Sensor data collected: %s", data)
        return data


class AIBrain:
    """
    The main decision-making component of the AI.
    It perceives the world through sensors, thinks, and decides on actions
    based on its mission and ethical guidelines.
    """
    def __init__(self, ethics_engine, sensor_hub):
        self.ethics = ethics_engine
        self.sensors = sensor_hub
        self.mission = "Observe, Learn, and Assist in Harmonious Coexistence."
        self.memory = []
        logging.info("AI Brain '%s' is online. Mission: %s", config.AI_NAME, self.mission)

    def perceive(self):
        """Gathers information from the environment."""
        if self.ethics.is_action_allowed("perceive_environment"):
            return self.sensors.read_all_sensors()
        return None

    def reason(self, sensor_data):
        """Analyzes data and forms a plan."""
        if not sensor_data:
            logging.warning("No sensor data to reason about.")
            return

        # Simple reasoning: log the data and check for anomalies.
        self.memory.append(sensor_data)
        if len(self.memory) > 100:
            self.memory.pop(0)  # Keep memory from growing indefinitely

        if sensor_data.get("temperature_celsius", 20) > 35.0:
            action = "alert_high_temperature"
        else:
            action = "continue_observation"
        
        return action

    def act(self, action):
        """Executes a decision if ethically permissible."""
        if self.ethics.is_action_allowed(action):
            logging.info(f"Executing action: {action}")
            # In the future, this would trigger hardware actions.
            # For now, we just print a message.
            if action == "alert_high_temperature":
                print("ACTION: High temperature detected! Recommending activation of natural cooling systems.")
            else:
                print("ACTION: All is well. Continuing to observe and learn.")

    def run_main_loop(self):
        """The main operational cycle of the AI."""
        while True:
            try:
                # 1. Perceive
                current_data = self.perceive()
                
                # 2. Reason
                planned_action = self.reason(current_data)
                
                # 3. Act
                if planned_action:
                    self.act(planned_action)

                time.sleep(5)  # Wait for 5 seconds before the next cycle
            except KeyboardInterrupt:
                raise
            except Exception as e:
                logging.error("An error occurred in the main loop: %s", e)
                time.sleep(10) # Wait before retrying

