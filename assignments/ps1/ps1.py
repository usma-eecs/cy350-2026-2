import os
import sys


def read_telemetry(file_path):
    """
    Reads telemetry data from the specified file.

    Each non-empty, non-comment line is parsed into a dictionary with keys:
    timestamp, altitude_km, temp_c, voltage, pitch, yaw, roll.

    Args:
        file_path (str): The path to the telemetry data file.

    Returns:
        tuple[list[dict], int]: A tuple of (telemetry_logs, count_invalid) where:
            - telemetry_logs is a list of parsed telemetry dictionaries
            - count_invalid is the number of lines that were invalid/corrupt and could not be parsed
    """

    telemetry_logs = []
    count_invalid = 0

    try:

        pass  # remove this line when you implement the function

        # TODO: open and read the telemetry data file at `file_path` line by line

        # TODO: iterate through each line of the file

        # TODO: ignore empty lines

        # TODO: ignore any empty lines and lines that contain comments starting with `#`

        # TODO: call `parse_telemetry_line` function to parse the line

        # TODO: handle the function return value appropriately, i.e. append to `telemetry_logs` if valid

        # TODO: handle errors gracefully!

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

    return telemetry_logs, count_invalid


def parse_telemetry_line(line):
    """
    Parses a single line of telemetry data and returns a dictionary with the relevant fields.

    Returns:
        dict: A dictionary with keys: timestamp, altitude_km, temp_c, voltage, pitch, yaw, roll.
        If the line is invalid or corrupt, returns False.

    Args:
        line (str): A line of telemetry data.
    """

    # TODO: strip and split the line into its components

    # TODO: ensure that the line is valid, i.e., it contains exactly 7 parts that are all numerical

    # TODO: ignore lines that do not contain the expected number of data fields

    # TODO: convert the components to their respective types and create the dictionary

    # TODO: return the dictionary if valid, otherwise return False

    # TODO: handle errors gracefully!

    return False


def find_apogee_event(telemetry_logs):
    """
    Finds the apogee event in the telemetry logs and returns the corresponding dictionary. Apogee is defined as the data point with the maximum altitude.
    """

    apogee_event = None

    # TODO: locate the apogee event

    return apogee_event


def get_min_voltage(telemetry_logs):
    """
    Finds the data point with the minimum voltage.

    Returns:
        The dictionary that contains the minimum voltage. If no data points are available, returns None.
    """

    min_voltage_event = None

    # TODO: locate the data point with the minimum voltage

    return min_voltage_event


def calculate_average_temperature(telemetry_logs):
    """
    Calculates the average temperature from the telemetry log.

    Returns:
        float: The average temperature in degrees Celsius. If no data points are available, returns None.
    """
    return None


def write_flight_summary(telemetry_logs, count_invalid, apogee_event, min_voltage, average_temperature, file_path):
    """
    Writes a flight summary to `file_path` with details about the apogee event, max tilt event, and time delta.

    If there are no valid telemetry logs, do not print the apogee or min voltage events or the average temperature.
    """

    pass

    # TODO: write the flight summary to `file_path`


if __name__ == "__main__":

    # if os is not linux, warn and exit
    if os.name != 'posix':
        print("This program should be run on Linux or WSL or docker. You may remove this check at your own risk.")
        sys.exit(1)

    # check command line arguments
    if len(sys.argv) < 2:
        script_name = os.path.basename(sys.argv[0])
        print(f"Usage: python {script_name} <input_file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "flight_summary.txt"

    telemetry_logs, count_invalid = read_telemetry(input_file)
    apogee_event = find_apogee_event(telemetry_logs)
    min_voltage = get_min_voltage(telemetry_logs)
    average_temperature = calculate_average_temperature(telemetry_logs)
    write_flight_summary(telemetry_logs, count_invalid, apogee_event, min_voltage, average_temperature, output_file)
