from flask import Flask, render_template
import RPi. GPIO as GPIO
import datetime
from time import sleep
import time
import serial
import MySQLdb
import pymysql

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)

#servo moter sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

p = GPIO.PWM(26, 100)
p.start(5)

#servo moter 90 reset
#angle = 90
#duty = float(angle) / 10.0 + 2.5
#p.ChangeDutyCycle(duty)
#time.sleep(1)
#sound left, right
soundL = 0
soundR = 0

app = Flask(__name__)

@app.route("/")
@app.route("/main")
def hello():
    dataVal = ser.readline()
    print dataVal
    value = dataVal.split()

    lightString = value[0]
    shockString = value[1]
    soundLString = value[2]
    soundRSTring = value[3]
    dustString = value[4]

    templateData = {
        'light': lightString,
      		'shock': shockString,
      		'soundL': soundLString,
      		'soundR': soundRSTring,
      		'dust': dustString
    }
    return render_template('main.html', **templateData)
#cctv
@app.route("/cctv.html")
def cctv():
    dataVal = ser.readline()
    print dataVal
    value = dataVal.split()

    lightString = value[0]
    shockString = value[1]
    soundLString = value[2]
    soundRSTring = value[3]
    dustString = value[4]

    templateData = {
        'light': lightString,
      		'shock': shockString,
      		'soundL': soundLString,
      		'soundR': soundRSTring,
      		'dust': dustString
    }

    return render_template('cctv.html', **templateData)
#shock
@app.route("/shock.html")
def shock():
    dataVal = ser.readline()
    print dataVal
    value = dataVal.split()

    lightString = value[0]
    shockString = value[1]
    soundLString = value[2]
    soundRSTring = value[3]
    dustString = value[4]

    templateData = {
        'light': lightString,
      		'shock': shockString,
      		'soundL': soundLString,
      		'soundR': soundRSTring,
      		'dust': dustString
    }

    return render_template('shock.html', **templateData)
    
#dust
@app.route("/dust.html")
def dust():
    dataVal = ser.readline()
    print dataVal
    value = dataVal.split()

    lightString = value[0]
    shockString = value[1]
    soundLString = value[2]
    soundRSTring = value[3]
    dustString = value[4]

    templateData = {
        'light': lightString,
      		'shock': shockString,
      		'soundL': soundLString,
      		'soundR': soundRSTring,
      		'dust': dustString
    }

    return render_template('dust.html', **templateData)

#led
@app.route("/light.html")
def light():
    dataVal = ser.readline()
    print dataVal
    value = dataVal.split()

    lightString = value[0]
    shockString = value[1]
    soundLString = value[2]
    soundRSTring = value[3]
    dustString = value[4]

    templateData = {
        'light': lightString,
      		'shock': shockString,
      		'soundL': soundLString,
      		'soundR': soundRSTring,
      		'dust': dustString
    }

    return render_template('light.html', **templateData)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)