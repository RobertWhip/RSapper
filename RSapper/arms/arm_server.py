#!/usr/bin/env python3
import socket
from socket_base import SocketBase 
from arms import Arms

class ArmServer (SocketBase):
	def __init__(self, connection, header_size, encoding):
		super().__init__(header_size, encoding)
		self.__arms = Arms()
	
	def start(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(connection)
		sock.listen(1)

		while True:
			try:
				client, address = sock.accept()
			except KeyboardInterrupt:
				client.close()
				sock.close()
				print("End.")
				break
			else:
				print("Client has connected:", address)
				while True:
					msg = super().receive_message(client)
					print(msg)
					self.__arms.move(msg)
				client.close()


if __name__ == '__main__':
	connection = ('', 8888)
	header_size = 10
	encoding = 'UTF-8'
	server = ArmServer(connection, header_size, encoding)
	server.start()
#