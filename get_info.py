import transport as t
import time
import thread


ip_list = [
"192.168.77.200",
]


def runCommand(host):
	with t.ssh_client(host) as client:
		return t.get_info_time(client)

if __name__ == "__main__":
	for ip in ip_list:
		start_time = time.time()
		time.sleep(5)
		try:
			table_time = runCommand(ip)
		except Exception as e:
			print('%s error!!!' % ip)
			# print('err' % e.value)
			print(e)
			continue
		print("ip %s done for %i seconds" % (ip, (time.time() - start_time)))
		print("****%s*****" % ip)
		print(table_time)