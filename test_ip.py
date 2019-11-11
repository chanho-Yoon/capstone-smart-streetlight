import RPi. GPIO as GPIO
from time import sleep
import time
import serial
import MySQLdb
import pymysql

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)

'''servo moter sensor'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

p = GPIO.PWM(26, 100)
p.start(5)
'''servo moter 90 reset'''

angle = 90
duty = float(angle) / 10.0 + 2.5
p.ChangeDutyCycle(duty)

'''sound left, right'''
soundL = 0
soundR = 0
db = pymysql.connect(host="localhost", user="root",
                     passwd="1234", db="kdn", charset='utf8')
curs = db.cursor()
circle_time = 1
dataVal = ser.readline()

while 1:
        dataVal = ser.readline()
        print dataVal
	value = dataVal.split() 

        light = value[0]
        shock = value[1]
        soundL = int(value[2])
        soundR = int(value[3])
        dust = value[4]

        if soundL > 150:
		angle = 40
                duty = float(angle) / 10.0 + 2.5
                p.ChangeDutyCycle(duty)
                time.sleep(6)
                try:
                        sql = "INSERT INTO sound (sensor_data, data_time) VALUES (%s , now())"
                        curs.execute(sql, (soundL))
                        db.commit()
                        print "---40 left"
                        print "End db commit"
                except:
                        print "Error: db commit"
                        db.rollback()
                soundR = 0

	elif soundR > 150:
		angle = 150
                duty = float(angle) / 10.0 + 2.5
                p.ChangeDutyCycle(duty)
	        time.sleep(6)
                try:
                        sql = "INSERT INTO sound (sensor_data, data_time) VALUES (%s , now())"
                        curs.execute(sql, (soundR))
                        db.commit()
                        print "----150 right"
                        print "End db commit"
	        except:
                        print "Error: db commit"
                        db.rollback()
                soundL = 0
        
        if shock != '0' :
                try:
                        sql = 'INSERT INTO shock (sensor_data, data_time) VALUES (%s, now())'
                        curs.execute(sql, (shock))
                        db.commit()
                        print "End db commit"
                        shock = '0'

                except:
                        print "Error: db commit"
                        db.rollback()

        if (circle_time%10)==0 :
                try:
                        sql = 'INSERT INTO light (sensor_data, data_time) VALUES (%s, now())'
                        curs.execute(sql, (light))
                        db.commit()

                        sql = 'INSERT INTO dust (sensor_data, data_time) VALUES (%s, now())'
                        curs.execute(sql, (dust))
                        db.commit()

                        print "End db commit"
                except:
                        print "Error: db commit"
                        db.rollback()
        
        time.sleep(2)
        circle_time += 1
