from curses import baudrate
import serial
import sqlite3

# Spek port
port = '/dev/ttyUSB0'
baudrate = 4800

# Setup konek port
ser = serial.Serial(port, baudrate)
print("connected to: " + ser.portstr)

# Baca isi port
baca_serial = ser.readline().decode('utf')
print(type(baca_serial))

# while True:
#     if ser.in_waiting:
#         print()