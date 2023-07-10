# Alarm
Raspberry Pi GPIO Alarm System
This project is a Raspberry Pi-based alarm system that leverages the GPIO Zero library in Python. It uses GPIO pins to control an array of LEDs to display digits, and buttons for user inputs. This is a fun and educational project for those who are interested in learning about hardware-software integration, GPIO manipulation, Python programming, and Raspberry Pi.

Project Overview:
The project involves the use of five buttons and eight LEDs arranged to represent a seven-segment display (plus an additional LED for alarm indication). Each button corresponds to a different function in the system: displaying a certain digit on the LED seven-segment display, showing a sequence of digits, and controlling the alarm system.

The alarm system is encapsulated in the Alarm class. This class maintains the state of the alarm and handles the button press events, updating the displayed digit and controlling the alarm LED accordingly.

The seven-segment display can show digits from 0 to 9. Each segment of the display is controlled by an individual LED connected to a specific GPIO pin on the Raspberry Pi.

The alarm is toggled ON and OFF using a dedicated method inside the Alarm class. When the alarm state is ON, a dedicated alarm LED is lit.

The project's main loop is continuously running, checking for any changes in button press events, updating the seven-segment display, and controlling the alarm LED based on the alarm state.

System Requirements:
Raspberry Pi (any model with GPIO pins)
Python 3.5 or above
GPIO Zero Library for Python
LEDs (8 in total)
Push Buttons (5 in total)
Jumper Wires, Resistors (as required)
Breadboard (optional, for easier circuit assembly)
How to Run:
To run the project, clone the repository, navigate to the project directory, and run the Python script.

bash
Copy code
git clone <repository-url>
cd <repository-directory>
python3 alarm.py
Save to grepper
Please make sure to connect all the GPIO pins, LEDs, and buttons as per the defined pin numbers in the script. Please use appropriate resistors to prevent any damage to the LEDs or Raspberry Pi. Be careful while handling the GPIO pins, as incorrect usage may damage your Raspberry Pi.
