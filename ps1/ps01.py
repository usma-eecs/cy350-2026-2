import os
import sys


def read_telemetry(file_path):
    """
    Reads the telemetry data from the specified file and returns a list of dictionaries.
    Each dictionary contains the keys: timestamp, altitude_km, temp_c, voltage, pitch, yaw, roll.

    Args:
        file_path (str): The path to the telemetry data file.

    Returns:
        list[dict]: A list of dictionaries with telemetry data.
    """

    telemetry_logs = []

    try:

        pass  # remove this line when you implement the function

        # TODO: open and read the telemetry data file at `file_path` line by line

        # TODO: iterate through each line of the file

        # TODO: ignore the lines that contain comments starting with `#`

        # TODO: ignore any empty lines or lines

        # TODO: call `parse_telemetry_line` function to parse the line

        # TODO: handle the function return value appropriately, i.e. append to `telemetry_logs` if valid

        # TODO: handle errors gracefully!

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

    return telemetry_logs


def parse_telemetry_line(line):
    """
    Parses a single line of telemetry data and returns a dictionary with the relevant fields.

    Returns:
        dict: A dictionary with keys: timestamp, altitude_km, temp_c, voltage, pitch, yaw, roll.
        If the line is invalid or corrupt,

    Args:
        line (str): A line of telemetry data.
    """

    # TODO: strip and split the line into its components

    # TODO: ensure that the line is valid, i.e., it contains exactly 7 parts that are all numerical

    # TODO: convert the components to their respective types and create the dictionary

    # TODO: return the dictionary if valid, otherwise return False

    return False


def find_apogee_event(telemetry_log):
    """
    Finds the apogee event in the telemetry log and returns the corresponding dictionary.

    Apogee is defined as the data point with the maximum altitude.
    """

    apogee_event = None

    # TODO: locate the apogee event

    return apogee_event


def get_min_voltage(telemetry_log):
    """
    Finds the data point with the minimum voltage.

    Returns:
        The dictionary that contains the minimum voltage. If no data points are available, returns None.
    """
    return None


def calculate_average_temperature(telemetry_log):
    """
    Calculates the average temperature from the telemetry log.

    Returns:
        float: The average temperature in degrees Celsius. If no data points are available, returns None.
    """
    return None


def write_flight_summary(telemetry_log, apogee_event, min_voltage, average_temperature, file_path):
    """
    Writes a flight summary to `file_path` with details about the apogee event, max tilt event, and time delta.
    """

    # TODO: write the flight summary to `file_path`


if __name__ == "__main__":

    # if os is not linux, warn and exit
    if os.name != 'posix':
        print("This script should be run on Linux or WSL or docker. You may remove this check at your own risk.")
        sys.exit(1)

    input_file = "telemetry_data.txt"
    output_file = "flight_summary.txt"

    telemetry_log = read_telemetry(input_file)
    apogee_event = find_apogee_event(telemetry_log)
    min_voltage = get_min_voltage(telemetry_log)
    average_temperature = calculate_average_temperature(telemetry_log)
    write_flight_summary(telemetry_log, apogee_event, min_voltage, average_temperature, output_file)
