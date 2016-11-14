import transport as t
import time
import thread
import pi_info as p
# -*- coding: utf-8 -*-

ip_list = [


"172.16.40.98", #kutuzova 1


"172.16.40.42", # Aralskaya 16
"172.16.40.10", #Vavilova
"172.16.40.246", # Svetlogorskaya 5
"172.16.40.78", # Kalinina 43


"172.16.40.54",  # Kalinina 169
"172.16.40.250", # Televizornaya
"172.16.0.218", # Metallurgov 51a
"172.16.40.58", # Kirova 125
"172.16.0.114", # Sverdlovskaya 15
"172.16.40.50", # Sverdlovskayay 8a
"172.16.40.242", # Aivazovskaya
"172.16.40.14", # 4 Shinnaya 20


"172.16.40.66", # Starii Skit 17
"172.16.40.62", # Moskovskoe 200e
"172.16.40.82", # Ujnaya 38a
"172.16.40.86", # Vaneeva/1
"172.16.40.90", # Maiskoe shosse


# "closed!!! 172.16.40.22", # 2 Bryanskaya
# "closed!!! 172.16.40.94", # Gladkova 22
]


shop_list = [ \
{"ip":"172.16.40.42", 	"name":"Aralskaya 16"} ,\
{"ip":"172.16.40.10", 	"name":"Vavilova"} ,\
{"ip":"172.16.40.246", 	"name":"Svetlogorskaya 5"} ,\
{"ip":"172.16.40.78", 	"name":"Kalinina 43"} ,\
{"ip":"172.16.40.54", 	"name":"Kalinina 169"} ,\
{"ip":"172.16.40.250", 	"name":"Televizornaya", 	"rekl_list":[]} ,\
{"ip":"172.16.0.218", 	"name":"Metallurgov 51a", 	"rekl_list":[]} ,\
{"ip":"172.16.40.58", 	"name":"Kirova 125", 		"rekl_list":[]} ,\
{"ip":"172.16.0.114", 	"name":"Sverdlovskayay 15", "rekl_list":[]} ,\
{"ip":"172.16.40.50", 	"name":"Sverdlovskayay 8a", "rekl_list":[]} ,\
{"ip":"172.16.40.66", 	"name":"Starii Skit 17", 	"rekl_list":[]} ,\
{"ip":"172.16.40.62", 	"name":"Moskovskoe 200e", 	"rekl_list":[]} ,\
{"ip":"172.16.40.82", 	"name":"Ujnaya 38a", 		"rekl_list":[]} ,\
{"ip":"172.16.40.86", 	"name":"Vaneeva/1", 		"rekl_list":[]} ,\
{"ip":"172.16.40.90", 	"name":"Maiskoe shosse", 	"rekl_list":[]} ,\
{"ip":"172.16.40.242", 	"name":"Aivazovskaya", 		"rekl_list":[]} ,\
{"ip":"172.16.40.22", 	"name":"2 Bryanskaya", 		"rekl_list":[]} ,\
{"ip":"172.16.40.14", 	"name":"4 Shinnaya 20", 	"rekl_list":[]} \
]

def runCommand(host):
	with t.ssh_client(host) as client:
		return p.get_info3(client, host)

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
		# print("ip %s done for %i seconds" % (ip, (time.time() - start_time)))
		print("***%s***\t---\t%s" % (ip, table_time))
		