from curses import baudrate
import serial
import sqlite3

# Spek port
port = '/dev/ttyUSB0'
baudrate = 4800

ser = serial.Serial(port, baudrate)
print("connected to: " + ser.portstr)

while True:
    if ser.in_waiting:
        print(ser.readline().decode('utf'))