#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os, sys
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600)

def controlar_luces():
	arduino.write(str.encode("L"))

def controlar_ventiladores():
	arduino.write(str.encode("V"))

def controlar_cortinas():
	arduino.write(str.encode("C"))

def encender():
	arduino.write(str.encode("I"))		

def apagar():
	arduino.write(str.encode("O"))

def cortinas_cerradas():
	arduino.write(str.encode("0"))

def cortinas_20():
	arduino.write(str.encode("1"))

def cortinas_40():
	arduino.write(str.encode("2"))

def cortinas_60():
	arduino.write(str.encode("3"))

def cortinas_80():
	arduino.write(str.encode("4"))

def cortinas_100():
	arduino.write(str.encode("5"))

def lectura_sensores():
	arduino.write(str.encode("S"))

def csv_write_data():
	if(arduino.in_waiting >0):
		line = arduino.readline()
		d_line = int(line.decode("utf-8"))
		if d_line == 1999:
			temp = arduino.readline()
			d_temp = int(temp.decode("utf-8"))
			lvl_f = arduino.readline()
			d_lvl_f = int(lvl_f.decode("utf-8"))
			hum = arduino.readline()
			d_hum = int(hum.decode("utf-8"))
			luz = arduino.readline()
			d_luz = int(luz.decode("utf-8"))
			print("temp=",d_temp," nivel= ",d_lvl_f," hum= ",d_hum," luz= ",d_luz)	
			with open('data.csv', 'a') as csvFile:
				row=[]
				writer = csv.writer(csvFile)
				writer.writerow([d_temp,d_lvl_f,d_hum,d_luz])
				#writer.writerows(row)
	#			csvFile.close()
