import paramiko
import time

user = "nda"
secret = "171086"
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

def add_mp3(client, list_mp3):
	client.exec_command('cd /home/pi/scripts && ./ftp_get_rekl_kras.sh')
	time.sleep(2)
	client.exec_command('cp /home/pi/scripts/kr_ritail_1.sh /home/pi/scripts/kr_ritail_1.sh.bak')
	client.exec_command('cat /home/pi/scripts/kr_ritail_1.sh | sed "/mpc next/d" > /home/pi/scripts/kr_ritail_1.tmp')
	client.exec_command('cat /home/pi/scripts/kr_ritail_1.tmp > /home/pi/scripts/kr_ritail_1.sh')
	for mp3 in list_mp3:
		time.sleep(2)
		client.exec_command('echo "\nmpg321 -g 38 /home/pi/pls2/svet_all' + str(mp3) +'.mp3 >> /home/pi/logs/svet_all' + str(mp3) + '.log" >> /home/pi/scripts/kr_ritail_1.sh')
	client.exec_command('echo "\nmpc next" >> /home/pi/scripts/kr_ritail_1.sh')
	time.sleep(2)	
	client.exec_command('cd /home/pi/scripts && ./volume_rekl.sh')


def delete_mp3(client, list_mp3):
	client.exec_command('cp /home/pi/scripts/kr_ritail_1.sh /home/pi/scripts/kr_ritail_1.sh.bak')
	for mp3 in list_mp3:
		client.exec_command('cat /home/pi/scripts/kr_ritail_1.sh | sed "/svet_all' + str(mp3) + '.mp3/d" > /home/pi/scripts/kr_ritail_1.tmp')
		time.sleep(2)
		client.exec_command('cat /home/pi/scripts/kr_ritail_1.tmp > /home/pi/scripts/kr_ritail_1.sh')
		time.sleep(3)

def change_mp3(client, list_mp3):
	for mp3 in list_mp3:
		client.exec_command('rm -f /home/pi/pls2/svet_all' + str(mp3) + '.mp3')
	time.sleep(10)
	client.exec_command('cd /home/pi/scripts && ./ftp_get_rekl_kras.sh')

def upload_script(client, scr, name):
	sftp = client.open_sftp()
	sftp.put(scr, '/home/pi/scripts/' + name)
	time.sleep(5)
	client.exec_command('cd /home/pi/scripts && chmod +x ' + name)

def get_info_time(client):
	stdin, stdout, stderr = client.exec_command('cd /home/pi/scripts && ./time_block.py')
	time.sleep(2)
	return stdout.read()
