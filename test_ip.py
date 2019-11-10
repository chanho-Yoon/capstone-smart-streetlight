
import serial
import MySQLdb
import pymysql
 
ser = serial.Serial('/dev/ttyACM0',9600)
db = pymysql.connect(host="localhost",user="root",passwd="1234",db="kdn",charset='utf8')
curs=db.cursor()

 
while 1:
        sonic = ser.readline()
	sonic = sonic.rstrip('\r\n')
        print sonic
        try:
                print "hi"
		sql = 'INSERT INTO test (sensor_data) VALUES (%s)'
                curs.execute(sql,(sonic))
                db.commit()
                print "End db commit"
 
        except:
                print "Error: db commit"
                db.rollback()
 

