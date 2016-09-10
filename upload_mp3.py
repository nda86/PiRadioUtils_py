import transport as t
import time
import thread


ip_list = [


# "172.16.40.94", # Gladkova 22


# "172.16.40.42", # Aralskaya 16
# "172.16.40.10", #Vavilova
# "172.16.40.246", # Svetlogorskaya 5
# "172.16.40.78", # Kalinina 43


# "172.16.40.54",  # Kalinina 169
# "172.16.40.250", # Televizornaya
# "172.16.0.218", # Metallurgov 51a
# "172.16.40.58", # Kirova 125
# "172.16.0.114", # Sverdlovskaya 15
# "172.16.40.50", # Sverdlovskayay 8a
# "172.16.40.242", # Aivazovskaya


# "172.16.40.66", # Starii Skit 17
# "172.16.40.62", # Moskovskoe 200e
# "172.16.40.82", # Ujnaya 38a
# "172.16.40.86", # Vaneeva/1
# "172.16.40.90", # Maiskoe shosse


# "172.16.40.22", # 2 Bryanskaya
# "172.16.40.14" # 4 Shinnaya 20
]


def runCommand(host):
	with t.ssh_client(host) as client:
		# t.add_mp3(client, [777])
		t.delete_mp3(client, [777])

if __name__ == "__main__":
	for ip in ip_list:
		start_time = time.time()
		time.sleep(5)
		try:
			runCommand(ip)
		except Exception as e:
			print('%s error!!!' % ip)
			# print('err' % e.value)
			print(e)
			continue
		print("ip %s done for %i seconds" % (ip, (time.time() - start_time)))

