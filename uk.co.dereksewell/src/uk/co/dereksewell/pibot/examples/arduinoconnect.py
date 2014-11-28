import serial # if you have not already done so

ser = serial.Serial('COM1', 9600)
ser.write('5')