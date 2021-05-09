import socket
import Serial

usbport = 'COM3'
board = serial.Serial(usbport,9600)
soc = socket.socket()
soc.bind((socket.gethostbyname(socket.gethostname()), 1234))
soc.listen(True)
connect, addr = soc.accept()

while (1):
	board.write(connect.recv(1024))