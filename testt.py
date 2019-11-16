from flask import Flask, render_template
import datetime
import os
from time import sleep
import time
import serial

while 1: 
        ser = serial.Serial('/dev/ttyACM0', 115200)
        dataVal = ser.readline()
        print (dataVal)
        val = dataVal.split(' ')
        print (val)

	sleep(1)
'''
	template_values = {
		'light' : val[0],
		'shock' : val[1],
		'sound' : val[2],
		'dust' : val[3]
	}
	
	path = os.path.join(os.path.dirname(__file__),'main.html')
	self.response.out.write(template.render(path, template_values))
'''	
       
	



