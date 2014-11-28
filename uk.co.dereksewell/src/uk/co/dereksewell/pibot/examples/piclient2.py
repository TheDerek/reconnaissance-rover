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


def forwards(ser):
    ser.write("f 1 255")
    time.sleep(0.1)
    ser.write("f 2 255")


def backwards(ser):
    ser.write("b 1 255")
    time.sleep(0.1)
    ser.write("b 2 255")


def right(ser):
    ser.write("f 1 255")
    time.sleep(0.1)
    ser.write("b 2 255")


def left(ser):
    ser.write("b 1 255")
    time.sleep(0.1)
    ser.write("f 2 255")

host = 'localhost'
port = 25565
size = 5024


while True:
    try:
        print "Attempting to connect to Arduino."

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

                    try:
                        locals()[data](ser)
                    except KeyError, message:
                        print "Non movement command received"

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