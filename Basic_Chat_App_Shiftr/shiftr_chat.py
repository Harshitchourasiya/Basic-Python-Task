import paho.mqtt.publish as publish
import paho.mqtt.subscribe as s
import thread
from time import sleep
from sys import stdout

i= 0

To = raw_input("Enter name of person to contact with : ")
From = raw_input("Enter your name : ")

def listener(a,b):
	while True:
		messgae_from= s.simple(To + "/" + From,
						hostname = "broker.shiftr.io",
						auth = {'username':"harharhar",'password':"harshit123"})
		stdout.write("\r" + messgae_from.payload +" "*len(From) + "\n")
		stdout.write(From + " : ")
		stdout.flush()
try:
	thread.start_new_thread(listener,("1","2"))
except Exception as ex:
	print ex

while True:
	message_to = raw_input(From + " : " )
	publish.single(From + "/" + To , message_to, 
					hostname = "broker.shiftr.io",
					auth = {'username':"harharhar",'password':"harshit123"})