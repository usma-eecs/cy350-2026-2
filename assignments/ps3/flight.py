import os
import json
import math
from data import TelemetryDataPoint

"""
This module defines RocketFlight class to process and analyze telemetry data from a rocket flight. This class manages a collection of data points and provides methods to analyze the entire flight data.
"""


class RocketFlight:
    """
    Manages a collection of TelemetryDataPoint instances and provides methods to analyze the flight data.
    Attributes:
        file_path (str): Path to the telemetry data file.
        flight_id (str): The name of the telemetry file without the extension.
        data_points (list): List of valid TelemetryDataPoint instances.
        corrupt_points_count (int): Count of corrupt data points.
    """

    def __init__(self, file_path):
        """
        Initializes the RocketFlight with a file path to the telemetry data.
        Args:
            file_path (str): Path to the telemetry data file.
        """

        # TODO: initialize all attributes

        self.file_path = file_path
        self.flight_id = os.path.basename(file_path)

    def load_data(self):
        """
        Loads and processes the telemetry data from the file.
        """
        self.data_points = []
        pass

    def get_apogee(self):
        """
        Returns:
            TelemetryDataPoint: The data point with the maximum altitude. If no data points are available, returns None.
        """
        return None

    def get_max_velocity(self):
        """
        Returns:
            TelemetryDataPoint: The data point with the maximum vertical velocity. If no data points are available, returns None.
        """
        return None

    def get_min_voltage(self):
        """
        Returns:
            TelemetryDataPoint: The data point with the minimum voltage. If no data points are available, returns None.
        """
        return None

    def calculate_average_velocity(self):
        """
        Calculates the average vertical velocity.
        Returns:
            float: The average vertical velocity in meters per second. If no data points are available, returns 0.0.
        """
        return 0.0

    def calculate_average_temperature(self):
        """
        Calculates the average temperature.
        Returns:
            float: The average temperature in degrees Celsius. If no data points are available, returns 0.0.
        """
        return 0.0

    def calculate_average_voltage(self):
        """
        Calculates the average voltage.
        Returns:
            float: The average voltage in volts. If no data points are available, returns 0.0.
        """
        return 0.0

    def generate_summary_json(self, output_path):
        """
        Generates a summary JSON file with flight statistics. If there are no valid data points, `valid_data_points` should be 0 and all statistics should be set to `None`. Use the `json` module to produce the JSON file.

        Args:
            output_path (str): Path to save the summary JSON file.
        """

        # TODO: create a dictionary with the required statistics

        # TODO: write the dictionary to a JSON file

        # See: https://docs.python.org/3/tutorial/inputoutput.html -> 7.2.2. Saving structured data with json

        return None
