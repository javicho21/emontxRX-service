import serial
import time
import paho.mqtt.client as paho
import datetime
import ssl

client = paho.Client()

# RaspberyPi conectado com Arduino via USB Cable / FTDI
#ser = serial.Serial("/dev/ttyACM0",9600)

# RaspberyPi conectado com Arduino usando modulo Bluetooth na ttyAMA0
ser = serial.Serial("/dev/ttyAMA0",9600)

# RaspberyPi conectado com Arduino usando modulo XBee na USB
#ser = serial.Serial("/dev/ttyUSB0",9600)

# MacBook rodando o script python e comunicando com Arduino via USB XBeeExplorer
#ser = serial.Serial("/dev/tty.usbserial-A800csue",19200)

# MacBook rodando o script python e comunicando com Arduino via cabo direto
#ser = serial.Serial("/dev/cu.usbmodem411",19200)

time.sleep(2)

timezone = "Eastern/US"
state = "NY"
city = "New York"
burrough = "Manhattan"
lname = "Vazquez"
fname = "Javier"
customerId = "12345678"

RPIhostname = "node-R2"
RPIip = "192.168.0.103"

client.connect("iot.eclipse.org", 1883, 60)

#uncoment next line to activate user authentication
#client.username_pw_set("azhang","********")

#uncoment next 2 lines for activate TLS
#client.tls_set("/etc/mosquitto/ca_certificates/ca.crt", certfile="/home/pi/myCA/client.crt", keyfile="/home/pi/myCA/client.key", cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
#client.connect("localhost", 8883, 60)

#coment next line if using TLS
client.connect("localhost", 1883, 60)

print "Waiting data from sensors ..."

while(1):
        time_stamp = int(time.time()*1000)
        RxTAGs = ser.readline()
        print (RxTAGs)
        mylist = RxTAGs.split(" ")

        emonTX_id = mylist[1]
        powerSensor1_L = int(mylist[2])
        powerSensor1_H = int(mylist[3])
        powerSensor2_L = int(mylist[4])
        powerSensor2_H = int(mylist[5])
        powerSensor3_L = int(mylist[6])
        powerSensor3_H = int(mylist[7])
        powerSensor4_L = int(mylist[8])
        powerSensor4_H = int(mylist[9])
        ACvoltage_L = int(mylist[10])
        ACvoltage_H = int(mylist[11])

        powerTot1 = (powerSensor1_H * 256) + powerSensor1_L
        powerTot2 = (powerSensor2_H * 256) + powerSensor2_L
        powerTot3 = (powerSensor3_H * 256) + powerSensor3_L
        powerTot4 = (powerSensor4_H * 256) + powerSensor4_L
        ACvoltage = ((ACvoltage_H *256) + ACvoltage_L)/100

        dataType = "METRIC"
        msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"emonTX.id":"%s","rpi.hostname": "%s","rpi.ip": "%s","rpi.datatype": "%s", "sensor.name": "%s","sensor.unit": "%s"},\nvalues: {"%s":"%s"}\n}]\n}' % ("Power",emonTX_id,RPIhostname,RPIip,dataType,"powerSensor1","Watts",time_stamp,powerTot1)
        print msg
        client.publish("javier/board1", msg)
        time.sleep(0.1)

        msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"emonTX.id":"%s","rpi.hostname": "%s","rpi.ip": "%s","rpi.datatype": "%s", "sensor.name": "%s","sensor.unit": "%s"},\nvalues: {"%s":"%s"}\n}]\n}' % ("Power",emonTX_id,RPIhostname,RPIip,dataType,"powerSensor2","Watts",time_stamp,powerTot2)
        print msg
        client.publish("javier/board1", msg)
        time.sleep(0.1)


        msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"emonTX.id":"%s","rpi.hostname": "%s","rpi.ip": "%s","rpi.datatype": "%s", "sensor.name": "%s","sensor.unit": "%s"},\nvalues: {"%s":"%s"}\n}]\n}' % ("Power",emonTX_id,RPIhostname,RPIip,dataType,"powerSensor3","Watts",time_stamp,powerTot3)
        print msg
        client.publish("javier/board1", msg)
        time.sleep(0.1)


        msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"emonTX.id":"%s","rpi.hostname": "%s","rpi.ip": "%s","rpi.datatype": "%s", "sensor.name": "%s","sensor.unit": "%s"},\nvalues: {"%s":"%s"}\n}]\n}' % ("Power",emonTX_id,RPIhostname,RPIip,dataType,"powerSensor4","Watts",time_stamp,powerTot4)
        print msg
        client.publish("javier/board1", msg)
        time.sleep(0.1)


        msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"emonTX.id":"%s","rpi.hostname": "%s","rpi.ip": "%s","rpi.datatype": "%s", "sensor.name": "%s","sensor.unit": "%s"},\nvalues: {"%s":"%s"}\n}]\n}' % ("ACvoltage",emonTX_id,RPIhostname,RPIip,dataType,"ACvoltage","Volts",time_stamp,ACvoltage)
        print msg
        client.publish("javier/board1", msg)
        time.sleep(0.1)

ser.close()

