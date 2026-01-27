# Rocket Data Processing

Tested Concepts: ability to define and use classes, handle exceptions, parse complex data into class instances, perform targeted data analysis using class methods, and generate structured output files.


## Recommended Resources

- [Python Docs Tutorial](https://docs.python.org/3/tutorial/)
- [f-strings](https://fstring.help/)


## Assignment Specific Restrictions - No Generative AI

For this refresher assignment, ***the use of Generative AI tools is prohibited.*** All other sources and assistance should be cited in accordance with the guidance found in the CY350 Syllabus located on the course's Canvas Syllabus page.

Use the provided starter files and fill in the missing parts to complete this assignment. Do not rename the files or change the class or function signatures.


## Scenario

Your previous data analysis program has been a success, and the SPEAR team is impressed with your ability to process and analyze the rocket's telemetry data. The team has received more refined data and now you are tasked with making your program more modular and extensible by implementing classes to capture your processing logic. You have decided to write a new Python script that defines two classes: `TelemetryDataPoint` and `RocketFlight`. These classes will encapsulate the functionality needed to parse, analyze, and summarize the telemetry data.

The team also wants to understand airframe stress to ensure the rocket's structural integrity during flight. To achieve this, you need to compute vertical velocity, which is not directly provided in the telemetry logs. You will need to calculate this from the altitude and timestamp data as follows:

> velocity = (current_altitude - previous_altitude) / (current_timestamp - previous_timestamp)

If previous data point is not available, set the velocity to zero.


## Key Tasks

All of the following methods are documented in the provided starter files.

1. Define class `TelemetryDataPoint` with the following methods:
   - `__init__()`
   - `calculate_velocity()`
   - `__str__()`

2. Define class `RocketFlight` with the following methods:
   - `__init__()`
   - `load_data()`
   - `get_apogee()`
   - `get_min_voltage()`
   - `get_max_velocity()`
   - `calculate_average_velocity()`
   - `calculate_average_temperature()`
   - `calculate_averages_voltage()`
   - `generate_summary_json()`


## Sample Input

```txt
# SPEAR Hypersonic Rocket - Full Telemetry Log
# Data format: timestamp,altitude_km,temp_c,voltage,pitch_deg,yaw_deg,roll_deg

1750000660,135.674,255.7,3.89,24.0,1.0,250
1750000666,136.980,ERROR,3.89,22.0,0.8,260
1750000700,142.408,295.6,3.87,16.0,0.2,290
1750000712,144.850,300.3,3.87,14.0,0.1,300
1750000748,148.329,315.7,UNDERVOLTAGE,6.0,-0.2,330
1750000760,149.031,320.4,3.85,0.0,-0.3,340
1750000772,149.488,318.9,3.84,-2.0,-0.4,350
1750000784,149.556,316.1,3.84,-4.0,-0.5,0
1750000788,149.551,312.6,3.83,-6.0,-0.6,10
1750000803,149.441,295.4,3.82,-12.0,-0.9,40
1750000818,149.186,288.7,3.81,-14.0,-1.0,50
1750000819,INVALID,288.7,3.80,-14.0,-1.0,50
```

## Sample Output

Create a JSON summary file with the following attributes:

Attributes:
- flight_id: the name of the telemetry file without the extension
- valid_data_points: count of valid telemetry data points
- corrupt_data_points: count of invalid telemetry data points, not including comments or empty lines
- max_altitude_km: maximum altitude in kilometers (float, rounded to 3 decimal places)
- max_altitude_timestamp: timestamp of the maximum altitude (int)
- max_velocity_m_s: maximum vertical velocity in meters per second (float, rounded to 2 decimal places)
- max_velocity_timestamp: timestamp of the maximum vertical velocity (int)
- min_voltage_v: minimum voltage (float, rounded to 2 decimal places)
- min_voltage_timestamp: timestamp of the minimum voltage (int)
- average_velocity_m_s: average vertical velocity in meters per second (float, rounded to 2 decimal places)
- average_temperature_c: average temperature in Celsius (float, rounded to 1 decimal place)
- average_voltage_v: average voltage (float, rounded to 2 decimal places)

See [Python Tutorial 7.2.2. Saving structured data with json](https://docs.python.org/3/tutorial/inputoutput.html).

### Expected Output for `telemetry_small.txt`

```json
{
    "flight_id": "telemetry_data_small",
    "valid_data_points": 9,
    "corrupt_data_points": 3,
    "max_altitude_km": 149.556,
    "max_altitude_timestamp": 1750000784,
    "max_velocity_m_s": 203.5,
    "max_velocity_timestamp": 1750000712,
    "min_voltage_v": 3.81,
    "min_voltage_timestamp": 1750000818,
    "average_velocity_m_s": 53.01,
    "average_temperature_c": 300.4,
    "average_voltage_v": 3.85
}
```

### Expected Output for `telemetry_big.txt`

```json
{
    "flight_id": "telemetry_big",
    "valid_data_points": 91,
    "corrupt_data_points": 6,
    "max_altitude_km": 149.556,
    "max_altitude_timestamp": 1750000784,
    "max_velocity_m_s": 1404.0,
    "max_velocity_timestamp": 1750000460,
    "min_voltage_v": 3.74,
    "min_voltage_timestamp": 1750001035,
    "average_velocity_m_s": 357.09,
    "average_temperature_c": 194.7,
    "average_voltage_v": 3.96
}
```
