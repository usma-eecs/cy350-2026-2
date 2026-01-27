from flight import RocketFlight
import os
import sys


def main():
    if os.name != "posix":
        print(
            "This script should be run on Linux or WSL or Docker. You may remove this check at your own risk."
        )
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Usage: python ps_04_solution.py <telemetry_file_path>")
        sys.exit(1)

    telemetry_file_path = sys.argv[1]
    # ensure file exists; otherwise, print error and exit
    if not os.path.isfile(telemetry_file_path):
        print(f"Error: File '{telemetry_file_path}' not found.")
        sys.exit(1)

    rocket_flight = RocketFlight(telemetry_file_path)
    rocket_flight.load_data()

    if not rocket_flight.data_points:
        print("No valid data points found.")
    else:
        print(
            f"{'Timestamp':^12} | {'Altitude (m)':^12} | {'Temp (C)':^8} | {'Volts':^5} | {'Velocity (m/s)':^14} | {'Attitude (p,y,r)'}"
        )

    for dp in rocket_flight.data_points:
        print(dp)
    print()

    summary_output_path = f"{rocket_flight.flight_id}_summary.json"
    rocket_flight.generate_summary_json(summary_output_path)

    print(f"Summary JSON saved to {summary_output_path}")


if __name__ == "__main__":
    main()
