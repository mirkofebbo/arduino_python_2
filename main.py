import tkinter as tk
import serial
import threading

# Initialize serial port
arduino = serial.Serial('COM5', 9600)

def update_sensor_value():
    while True:
        if arduino.inWaiting() > 0:
            sensor_value.set(arduino.readline().decode('utf-8').strip())
            root.update_idletasks()

def led_on():
    arduino.write(b'H')

def led_off():
    arduino.write(b'L')

# Create the main window
root = tk.Tk()
root.title("Arduino LED and Sensor Control")

sensor_value = tk.StringVar()
sensor_label = tk.Label(root, textvariable=sensor_value)
sensor_label.pack()

# Create and place buttons
on_button = tk.Button(root, text="LED ON", command=led_on)
on_button.pack()

off_button = tk.Button(root, text="LED OFF", command=led_off)
off_button.pack()

# Start the thread to update sensor value
thread = threading.Thread(target=update_sensor_value)
thread.daemon = True
thread.start()

# Run the application
root.mainloop()
