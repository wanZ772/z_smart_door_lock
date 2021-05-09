import serial
from threading import Thread
import socket
try:
	usbport = 'COM3'
	board = serial.Serial('COM3', 9600)
except:
	pass
soc = socket.socket()

soc.bind((socket.gethostbyname(socket.gethostname()), 1234))
# soc.listen(True)
# connect, addr = soc.accept()
# board.write(connect.recv(1024))
soc.listen(True)
connect, addr = soc.accept()
def keep_connect():
	global connect
	global addr
	while (1):
		soc.listen(True)
		connect, addr = soc.accept()

def keep_control():
	global connect
	while (1):
		board.write(connect.recv(1024))
keep_controlling = Thread(target = keep_control)
keep_connection = Thread(target = keep_connect)

keep_connection.start()
keep_controlling.start()