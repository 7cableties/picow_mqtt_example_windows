import serial # version serial==0.0.97
import time

###
# This script waits for a connection to a COM port (e.g. COM3), and prints any serial output.
# I find this to be better alternative to PuTTY, as you don't have to keep starting the session.  
#
# Run this script from a dedicated terminal (cmd/powershell).
###


# Change these params as needed
port = "COM3"
baud_rate = 9600

while True:
    try:
        with serial.Serial(port, baud_rate, timeout=1) as ser:
            print("Connected to " + port)
            while True:
                line = ser.readline().decode(errors="ignore").strip()
                if line:
                    print(line)
    except serial.SerialException:
        print("Waiting for " + port +"...")
        time.sleep(1)
