from curses import baudrate
import serial
import sqlite3

ser = serial.Serial(port='/dev/ttyUSB0',baudrate=4800,parity=serial.PARITY_NONE)
print("connected to: " + ser.portstr)
print(ser.readline())