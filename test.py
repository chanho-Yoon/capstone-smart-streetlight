import RPi. GPIO as GPIO
from time import sleep
import time
import serial
ser = serial.Serial('/dev/ttyACM0',9600)


'''servo moter sensor'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

p = GPIO.PWM(26,100)
p.start(5)
'''servo moter 90 reset'''
angle = 90
duty = float(angle) / 10.0 + 2.5
p.ChangeDutyCycle(duty)
time.sleep(1)
'''sound left, right'''
soundL=0
soundR=0
	
while 1 :
	dustVal = ser.readline()
	print dustVal
	
	value = dustVal.split();	
	
	soundL = int(value[2])
	soundR = int(value[3])
	
	if soundL > 140 :
		angle = 40
                duty = float(angle) / 10.0 + 2.5
                p.ChangeDutyCycle(duty)
		print "40-----"
		time.sleep(6)
		angle = 90 
                duty = float(angle) / 10.0 + 2.5
                p.ChangeDutyCycle(duty)
		soundR = 0
		
		
	elif soundR > 140 :
		angle = 150
                duty = float(angle) / 10.0 + 2.5
                p.ChangeDutyCycle(duty)
		print "150----"
		time.sleep(6)
		angle = 90 
                duty = float(angle) / 10.0 + 2.5
                p.ChangeDutyCycle(duty)
		soundL = 0