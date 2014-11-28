"""
The client for serverecho.py
"""

import socket
import serial
import time
import thread
from datetime import datetime

def releaseMotors(ser):
    ser.write("r 1 255")
    time.sleep(0.1)
    ser.write("r 2 255")

def matchCounter(breakThread, ser):
    breakThread = False
    lagTime = 0
    while not breakThread and (lagTime < 0.3):
        time.sleep(0.01)
        lagTime += 0.01

    if not breakThread:
        releaseMotors(ser)

breakThread = False
host = 'localhost'
port = 25565
size = 5024

attempt2 = True
timeLastReceived = 0

while True:
    try:
        print "Attempting to connect to Arduino."

        if attempt2:
            attempt2 = False
            ser = serial.Serial('COM3', 115200)

        else:
            attempt2 = True
            ser = serial.Serial('COM3', 115200)


        ser.setDTR(False)
        print "Connected to Arduino"
        while True:
            releaseMotors(ser)
            try:
                print "Attempting Connection to server"
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                print "Connected to Server"
                while True:
                    data = s.recv(size)
                    print data

                    ser.write(data)
                    time.sleep(0.01)
                    breakThread = True

            except socket.error, (value,message):
                if s:
                    s.close()
                print "Connection Failed: " + message
    except serial.serialutil.SerialException, message:
        print message





 #Key:
    #xyzzz
    #x = motor, 1 or 2
    #y = type:
        #f = forwards
        #b = backwards
        #r = Release

        #zzz = power from 0-255