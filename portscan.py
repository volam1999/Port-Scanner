import socket
from IPy import IP

class PortScanner():
	def __init__(self, target, port_num):
		self.target = target
		self.port_num = port_num

	def scan(self):
		for port in range(1, self.port_num):
			self.scan_port(port)

	def check_ip(self):
		try:
			IP(self.target)
			return self.target
		except ValueError:
			return socket.gethostbyname(self.target)

	def scan_port(self, port):
		try:
			converted_ip = self.check_ip()
			sock = socket.socket()
			sock.settimeout(0.07)
			sock.connect((converted_ip, port))
			try:
				banner = sock.recv(1024)
				print('[+] Open port ' + str(port)+ ':' +str(banner.decode().strip("\n")))
			except:
				print('[+] Open port ' + str(port))
			sock.close()
		except Exception as e:
			pass

		


