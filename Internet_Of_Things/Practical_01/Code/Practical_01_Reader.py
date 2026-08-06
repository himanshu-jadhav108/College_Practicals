# Practical 1: Python Serial Reader for TMP36 Data
import time
import serial

PORT = "COM3"      # Windows: COM3 / Linux: /dev/ttyACM0
BAUD = 9600

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)  # Wait for Arduino reset
    print(f"Connected to {PORT} at {BAUD} baud.")
    
    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print("Received:", line)
except KeyboardInterrupt:
    print("Stopped by user.")
except Exception as e:
    print("Serial error:", e)
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
