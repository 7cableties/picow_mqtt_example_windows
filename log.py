import serial
import time

while True:
    try:
        with serial.Serial("COM3", 9600, timeout=1) as ser:
            print("Connected to COM3")
            while True:
                line = ser.readline().decode(errors="ignore").strip()
                if line:
                    print(line)
    except serial.SerialException:
        print("Waiting for COM3...")
        time.sleep(1)
