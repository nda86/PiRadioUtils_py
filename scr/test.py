
def foo(list_mp3):
	cmd = 'cat /home/pi/scripts/kr_ritail_1.sh | sed "/svet_all00.mp3/d; '
	for mp3 in list_mp3:
		cmd =  cmd + ' /svet_all' + str(mp3) + '.mp3/d; '
	cmd = cmd + '" > /home/pi/scripts/kr_ritail_1.tmp'
	print cmd

if __name__ == "__main__":
	foo([12,25,26,28,56])
