#!/usr/bin/env python3
import socket
from socket_base import SocketBase
from kinect_arms import KinectArms
import time


class ArmClient (SocketBase):
	def __init__(self, connection, header_size, encoding, reconnect_seconds):
		super().__init__(header_size, encoding)
		self.__kinect_arms = KinectArms()

	def start(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			while True:
				try:
					sock.connect(connection)
				except:
					time.sleep(reconnect_time)
					continue
				while True:
					msg = str(self.__kinect_arms.get_arm_coords())
					#print("Sending:", msg)
					super().send_message(sock, msg)
					time.sleep(0.5)
				
		except:
			sock.close()
			print("End.")


if __name__ == '__main__':
	connection = ('127.0.0.1', 8888)
	header_size = 10
	encoding = 'UTF-8'
	reconnect_seconds = 5
	client = ArmClient(connection, header_size, encoding, reconnect_seconds)
	client.start()
#