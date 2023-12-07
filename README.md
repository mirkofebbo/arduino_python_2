# Arduino-Python LED Control
## Overview
This project demonstrates how to control the built-in LED on an Arduino Uno using a Python-based graphical user interface (GUI). The Python script communicates with the Arduino over a serial connection, sending commands to turn the LED on or off based on user input.

# Requirements
## Hardware
Arduino Uno
USB Cable 

## Software
Arduino IDE
Python 3
PySerial library (Python)
Tkinter library (Python)

# Setup
## Arduino Setup
Connect your Arduino Uno to your computer.
Open the Arduino IDE and upload the serial_demo.ino file to the Arduino:

## Python Environment Setup

### Install the PySerial library using pip:

pip install pyserial

Modify the serial port in the script to match the port your Arduino is connected to. For example, replace 'COM5' with your Arduino's port name.

### Run the script:

bash
Copy code
python led_control.py
A GUI window with "LED ON" and "LED OFF" buttons will appear.

Use these buttons to control the LED on your Arduino.

## Troubleshooting
Ensure that the correct serial port is specified in the Python script.
Close the Arduino IDE's serial monitor before running the Python script to avoid serial port conflicts.
Check your connections and ensure that the Arduino is properly powered.

License
MIT License

Author
Mirko Febbo

