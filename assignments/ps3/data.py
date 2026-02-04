import json
import math

"""
This module defines TelemetryDataPoint, which represents a single data point. This class is not responsible for managing collections of data points; it simply encapsulates the data and behavior of an individual line of telemetry data.
"""


class TelemetryDataPoint:
    """
    Represents a single telemetry data point from the rocket flight.
    Attributes:
        timestamp (int): The time in seconds since launch.
        altitude (float): The altitude in meters.
        temperature (float): The temperature in degrees Celsius.
        voltage (float): The battery voltage in volts.
        attitude (tuple): A tuple of three floats representing pitch, yaw, and roll in degrees
        is_valid (bool): Indicates if the data point is valid or corrupt.
    """

    def __init__(self, raw_line, last_data_point=None):
        """Initializes a TelemetryDataPoint from a raw data line by extracting relevant fields and assigning them to class attributes."""
        pass

        # TODO: what to do here?

    def calculate_velocity(self, last_data_point):
        """
        Calculates the vertical velocity based on the change in altitude and time. If there is no previous data point or if the time difference is zero, the velocity should be 0.0.
        Args:
            last_data_point (TelemetryDataPoint): The previous valid data point.
        Returns:
            float: The vertical velocity in meters per second.
        """

        # TODO: look at last_data_point to get previous altitude and timestamp

        # TODO: calculate the difference in altitude and time

        # TODO: divide the two numbers to get velocity

        # TODO: ensure correct units!!

        return 0.0

    def __str__(self):
        """
        __str__ method provides any class with a string representation.

        See main.py for the expected format.

        See https://fstring.help/ and https://docs.python.org/3/tutorial/inputoutput.html

        Returns:
            str: Formatted string of the data point.
        """
        return "Not Implemented"
