import paramiko
import time
import datetime as dt

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

def add_mp3_tail(client, list_mp3):
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
	cmd = 'cat /home/pi/scripts/kr_ritail_1.sh | sed "/svet_all00.mp3/d; '
	for mp3 in list_mp3:
		cmd =  cmd + ' /svet_all' + str(mp3) + '.mp3/d; '
	cmd = cmd + '" > /home/pi/scripts/kr_ritail_1.tmp'
	client.exec_command(cmd)
	time.sleep(8)
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
	client.exec_command('sed -i "s/$\r//g" /home/pi/scripts/' + name)
	client.exec_command('cd /home/pi/scripts && chmod +x ' + name)

def download_script(client, path_from, path_to):
	sftp = client.open_sftp()
	sftp.get(path_from, path_to)

def get_info_time(client):
	stdin, stdout, stderr = client.exec_command('cd /home/pi/scripts && ./time_block.py')
	time.sleep(2)
	return stdout.read()

def backup_kr(client):
	now = dt.datetime.now()
	date = now.strftime("%d-%m-%y_%H-%M")
	client.exec_command('cp /home/pi/scripts/kr_ritail_1.sh /home/pi/scripts/' + str(date) + '_kr_ritail_1.bak')

def strip(client):
	client.exec_command('sed -i.strip "/^$/d; /^#[^!]/d" /home/pi/scripts/kr_ritail_1.sh')

def add_mp3_head(client, list_mp3):
	client.exec_command('cd /home/pi/scripts && ./ftp_get_rekl_kras.sh')
	time.sleep(2)
	client.exec_command('cp /home/pi/scripts/kr_ritail_1.sh /home/pi/scripts/kr_ritail_1.sh.bak')
	client.exec_command('sed -i.head "1,2d" /home/pi/scripts/kr_ritail_1.sh')
	txt = '#!\/bin\/bash\\nmpc pause\\n'
	for mp3 in list_mp3:
		time.sleep(2)
		txt = txt + 'mpg321 -g 38 \/home\/pi\/pls2\/svet_all' + str(mp3) +'\.mp3 >> \/home\/pi\/logs\/svet_all' + str(mp3) + '\.log\\n'
	stdin, stdout, stderr = client.exec_command('sed -i "1s/^/' + str(txt) + '/" /home/pi/scripts/kr_ritail_1.sh')
	# print stderr.readlines()
	time.sleep(2)	
	client.exec_command('cd /home/pi/scripts && ./volume_rekl.sh')

	# sed -i "1s/^/#!\/bin\/bash\nmpc pause\nmpg321 -g 38 \/home\/pi\/pls2\/svet_all' + str(mp3) +'\.mp3 >> \/home\/pi\/logs\/svet_all124\.log\n/" /home/pi/scripts/kr_ritail_1.sh
