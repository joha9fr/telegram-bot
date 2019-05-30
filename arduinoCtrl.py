#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os, sys
import serial
import csv

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

def get_sensor_data():
	with open('data.csv', 'r') as csv_file:
		data=list(csv.reader(csv_file))[-1]
	return data

