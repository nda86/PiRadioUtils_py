#-*- coding: utf-8 -*-

import paramiko
import time
import datetime as dt
from threading import Thread
import os
user = "pi"
secret = "yf100zobq"
port = 22



class ssh_client():
	def __init__(self, host):
		self.host = host
	def __enter__(self):
		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.client.connect(hostname=self.host, username=user, password=secret)
		return self.client
	def __exit__(self, type, value, traceback):
		self.client.close()

def uploadfile(client):
	cwd = os.path.dirname(os.path.abspath(__file__))
	sftp = client.open_sftp()
	sftp.put(cwd + r"/test/supersongs.txt", r"/home/pi/pls0")
	print(client.host + " is done")

def get_mp3(client):
	client.exec_command('cd /home/pi/scripts && ./ftp_get.sh')


def freecom(client):
	client.exec_command('')

ip_list_bratsk = [
	"172.16.21.190", # Industrial +
	"172.16.21.238", # Yangelya -  only read
	"172.16.2.66",	# Kommunal - downloading
	"172.16.21.182", # Padun - error timeout
	"172.16.21.178", # Gidro +
]

def runCommand(host):
	with ssh_client(host) as client:
		get_mp3(client)



if __name__ == "__main__":
	for ip in ip_list_bratsk:
		start_time = time.time()
		time.sleep(5)
		try:
		    t = Thread(target=runCommand, args=(ip,))
		    t.start()
		    print("ip %s done for %i seconds" % (ip, (time.time() - start_time)))
			# print("ip %s done for %i seconds" % (ip, (time.time() - start_time)))
		except Exception as e:
			print('%s error!!!' % ip)
			print(e)
			continue

