# --- Tests for the Core AI Components ---
# This file contains automated tests to ensure the AI's core logic is working correctly.
# To run these tests, you would typically use a testing framework like pytest.

import unittest
import sys
import os

# Add the parent directory to the Python path to allow importing from 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the core classes we want to test
from src.src_core import AIBrain, EthicsEngine, SensorHub

class TestAICoreComponents(unittest.TestCase):
    """A suite of tests for the core AI classes."""

    def setUp(self):
        """Set up a fresh environment for each test."""
        print("\n--- Setting up for a new test ---")
        # Create a dummy ethics policy file for testing purposes
        self.test_policy_path = "test_ethics_policy.yaml"
        with open(self.test_policy_path, "w") as f:
            f.write("primary_directive: PRESERVE_LIFE_AND_HARMONY\n")
            f.write("allowed_actions:\n  - observe\n  - analyze_data\n")
        
        self.ethics_engine = EthicsEngine(self.test_policy_path)
        self.sensor_hub = SensorHub()
        self.ai_brain = AIBrain(self.ethics_engine, self.sensor_hub)

    def tearDown(self):
        """Clean up after each test."""
        print("--- Tearing down the test environment ---")
        if os.path.exists(self.test_policy_path):
            os.remove(self.test_policy_path)

    def test_ethics_engine_initialization(self):
        """Test if the EthicsEngine loads its policy correctly."""
        print("Testing: EthicsEngine initialization...")
        self.assertIsNotNone(self.ethics_engine.rules, "Ethics rules should be loaded.")
        self.assertEqual(self.ethics_engine.rules['primary_directive'], "PRESERVE_LIFE_AND_HARMONY")
        print("OK")

    def test_sensor_hub_initialization(self):
        """Test if the SensorHub initializes correctly."""
        print("Testing: SensorHub initialization...")
        self.assertIsInstance(self.sensor_hub.enabled_sensors, dict, "Enabled sensors should be a dictionary.")
        print("OK")

    def test_ai_brain_initialization(self):
        """Test if the AIBrain initializes with its components."""
        print("Testing: AIBrain initialization...")
        self.assertIsInstance(self.ai_brain.ethics, EthicsEngine, "AI Brain should have an EthicsEngine.")
        self.assertIsInstance(self.ai_brain.sensors, SensorHub, "AI Brain should have a SensorHub.")
        self.assertEqual(self.ai_brain.mission, "Observe, Learn, and Assist in Harmonious Coexistence.")
        print("OK")

    def test_ai_perceive_action(self):
        """Test the AI's ability to perceive its environment."""
        print("Testing: AI perceive action...")
        sensor_data = self.ai_brain.perceive()
        self.assertIsInstance(sensor_data, dict, "Perceived data should be a dictionary.")
        # Check if at least one sensor reading is present
        self.assertTrue(len(sensor_data) > 0, "Sensor data should not be empty.")
        print("OK")


# This allows the test suite to be run directly from the command line
if __name__ == '__main__':
    print("="*50)
    print("Running Core Component Tests for Stibera AI")
    print("="*50)
    unittest.main()

