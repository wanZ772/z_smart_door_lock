import socket
import os
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.utils import rgba
Window.size = (300,500)
from threading import Thread
from kivy.clock import Clock
from kivy.properties import ObjectProperty
# soc = socket.socket()
# soc.connect(('192.168.43.15', 1234))
# while (1):
	# command = input('Comamnd: ')
	# if (command == '1'):
		# soc.send('open'.encode())
	# else:
		# soc.send('close'.encode())

class Controller(Screen):
	def recheck_connection(self):
		with open('connection_status.log', 'r') as connection_status:
			status = connection_status.read()
			if (status == '1'):
				self.ids.connection_name.text = "Connected to: " + target_door
			else:
				pass
	def connect(self):
		global soc
		global target_door
		with open('connection_status.log', 'w') as write_status:
			write_status.write('0')
		try:
			with open('door.log', 'r') as read_file:
				target_door = read_file.read()
			soc = socket.socket()
			connection_test = soc.connect((target_door, 1234))
			read_file.close()
			with open('connection_status.log', 'w') as write_status:
				write_status.write('1')
		except:
			pass
	def write_door(self):
		with open('door.log', 'w') as write_status:
			write_status.write(self.ids.new_door.text)
		# self.ids.new_door.text = ''
	def show_connection(self, *args):
		# self.connection_name.text = "Connected to: " + target_door
		# print(self.ids.connection_name.text)
		# connection_name = ObjectProperty(None)
		self.ids.connection_name.text = "Connected to: " + target_door
		print(1)
	def __init__(self, **kwargs):
		super(Controller, self).__init__(**kwargs)
		with open('connection_status.log', 'r') as connection_status:
			status = connection_status.read()
		if (status == '1'):
			Clock.schedule_once(self.show_connection)
		else:
			pass
	def remove_doors(self):
		os.remove('door.log')
	def open_door(self):
		self.ids.status_id.background_color = rgba('#4287f5')
		self.ids.status_id.text = "Door Status: Opened"
		soc.send('open'.encode())
		
	def close_door(self):
		self.ids.status_id.background_color = (1,0,0,1)
		self.ids.status_id.text = "Door Status: Closed"
		soc.send('close'.encode())
	# connection_name = ObjectProperty(None)
	# Clock.schedule_once(Controller.open_door(), 0.1)
class MyApp(MDApp):
	global soc
	global target_door
	with open('connection_status.log', 'w') as write_status:
		write_status.write('0')
	try:
		with open('door.log', 'r') as read_file:
			target_door = read_file.read()
		soc = socket.socket()
		connection_test = soc.connect((target_door, 1234))
		read_file.close()
		with open('connection_status.log', 'w') as write_status:
			write_status.write('1')
	except:
		pass
	# def on_close(self):
		# soc.close()
	# def on_start(self):
		# Clock.schedule_interval(Controller.show_connection, 1)
		# pass
	def build(self):
		
		return Controller()
if '__main__' == __name__:
	MyApp().run()