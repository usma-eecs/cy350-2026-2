# Rocket Data Processing

Tested Concepts: read a file, parse data into dictionaries, handle common data errors, perform basic calculations, use a loop for targeted data analysis, and write structured, formatted data to a new file.

## Assignment Specific Restrictions
For this refresher assignment, ***the use of Generative AI tools is prohibited.*** All other sources and assistance should be cited in accordance with the guidance found in the CY350 Syllabus located on the course's Canvas Syllabus page.

## Scenario

https://www.westpoint.edu/news/press-releases/class-of-2025-west-point-cadets-break-record-hypersonic-rocket-launch

You have graduated from CY300 and joined the SPEAR hypersonic rocket team. The latest hypersonic rocket has completed its test flight, and the raw telemetry data has been saved to a file named telemetry.txt. Each line in the file is supposed to represent a single data point containing a timestamp, altitude in kilometers, a temperature reading in Celsius, and the battery voltage. However, the transmission was partially corrupted during the high-speed flight. Some lines contain comments, and others have malformed or missing data. Your mission is to write a Python script that can reliably parse this file, structure it for easier analysis, and generate a clean `flight_summary.txt` file. You also need to pinpoint the exact moment the rocket reached its apogee, which is the highest point in its flight (maximum altitude). The rocket contains a solar panel that powers its systems, so the battery voltage may fluctuate significantly during the flight.

## Key Tasks

1. Create Data Lists: Before you start processing the file, create three empty lists: one for altitude, one for temperature, and one for voltage.

2. Read the File: Open and read the `telemetry.txt` file line by line. The input file contains the following data format:

   ```
   timestamp, altitude_km, temperature_celsius, voltage
   ```

	- timestamp: Unix timestamp (integer)
	- altitude_km: Altitude in kilometers (float)
	- temperature_celsius: Temperature in Celsius (float)
	- voltage: Battery voltage (float)

	The file may or may not have a header line, but if it does, it will start with `#` indicating a comment. Make no assumptions and simply ignore any lines that start with `#` or are empty.

3. Iterate and Parse: Iterate through each line of the file. Ignore the lines that contain comments starting with `#`. Also ignore any empty lines or lines. Use the built-in string methods to [strip](https://diveintopython.org/functions/string-methods/strip) and [split](https://diveintopython.org/functions/string-methods/split) each valid line into its components.

4. Validate the Data: A valid line must contain exactly seven parts. Timestamp should be integer. All other parts (altitude, temperature etc.) must be convertible to a float. Skip lines that do not conform to the expected format, e.g. `MALFORMED_DATA`.

5. Create the dictionary: If a line is valid, convert the altitude, temperature, voltage, pitch, yaw, roll to floats and add them to a dictionary representing a data point. If no valid data is found, set the maximum altitude, minimum voltage, and average temperature to 0.0.

6. Calculate Statistics: After processing all lines, calculate and display the following statistics:

	- Count of how many lines were valid and how many were corrupt
	- Maximum altitude
	- Minimum voltage
	- Average temperature

7. Display the Results: Print the results formatted as displayed in the sample output. Note that:

	- Counts of data points should be integers.
	- Maximum altitude should be a float rounded to one decimal place.
	- Minimum voltage should be a float rounded to two decimal places.
	- Average temperature should be a float rounded to one decimal place.

## Sample Input

Filename: `telemetry_small.txt` and `telemetry_big.txt`

These files contain a large number of data points that your script will read. It contains a mix of valid data, comments, and errors. General format of the file is as follows:

### Attributes:
- timestamp (int)
- altitude_km (float)
- temperature_celsius (float)
- voltage (float)
- pitch_deg (float)
- yaw_deg (float)
- roll_deg (float)

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

Filename: `flight_summary.txt`

For the sample input above, the output should look like this:

```txt
Rocket Telemetry Analysis
-------------------------
Valid data points: 6
Corrupt data points: 3
Maximum Altitude: 149.6 km
Average Temperature: 24.3 C
Average Voltage: 3.90 V
```

The `telemetry_big.txt` file will result in the following output:

```txt
Rocket Telemetry Analysis
-------------------------
Valid data points: 95
Corrupt data points: 5
Maximum Altitude: 149.6 km
Average Temperature: 272.3 C
Average Voltage: 3.95 V
```
