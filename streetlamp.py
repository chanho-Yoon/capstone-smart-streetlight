from flask import Flask, render_template
import RPi. GPIO as GPIO
import datetime
from time import sleep
import time
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

#servo moter sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

p = GPIO.PWM(26, 100)
p.start(5)
#servo moter 90 reset
angle = 90
duty = float(angle) / 10.0 + 2.5
p.ChangeDutyCycle(duty)
time.sleep(1)
#sound left, right
soundL = 0
soundR = 0

app = Flask(__name__)

@app.route("/")

#def hello():
#	now = datetime.datetime.now()
#	timeString = now.strftime("%Y-%m-%d %H:%M:%S")
#	templateData = {
#		'title' : 'Raspberry Pi 3',
#		'time' : timeString
#	}
#	return render_template('index.html' , **templateData)


def hello():
    dataVal = ser.readline()
    value = dataVal.split()

    soundL = int(value[2])
    soundR = int(value[3])
    if soundL > 140:
        angle = 40
        duty = float(angle) / 10.0 + 2.5
        p.ChangeDutyCycle(duty)
        print "40-----"
        time.sleep(6)
        angle = 90
        duty = float(angle) / 10.0 + 2.5
        p.ChangeDutyCycle(duty)
        soundR = 0

    elif soundR > 140:
        angle = 150
        duty = float(angle) / 10.0 + 2.5
        p.ChangeDutyCycle(duty)
        print "150----"
        time.sleep(6)
        angle = 90
        duty = float(angle) / 10.0 + 2.5
        p.ChangeDutyCycle(duty)
        soundL = 0

    lightString = value[0]
    shockString = value[1]
    soundLString = value[2]
    soundRSTring = value[3]
    dustString = value[4]

    templateData = {
        'light' : lightString,
		'shock' : shockString,
		'soundL' : soundLString,
		'soundR' : soundRSTring,
		'dust' : dustString
	}
	
    return render_template('index.html',**templateData)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)