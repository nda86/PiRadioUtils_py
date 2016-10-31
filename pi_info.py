import transport as t
import time
from mutagen.mp3 import MP3


# duration
def get_info2(client, ip):
	t.download_script(client, "/home/pi/scripts/kr_ritail_1.sh", "./tmp/kr_ritail_1_" + ip +".txt")
	time.sleep(5)
	with open("./tmp/kr_ritail_1_" + ip + ".txt") as f:
		all_duration = 0
		for line in f:
			if line[0] is "#":
				continue
			l = line.split(" ")
			if len(l) > 3:
				path = l[3]
				track = path.split("/")[4]
				audio = MP3("./pls/" + track)
				duration = round(audio.info.length)
				# print(str(audio["TPE1"]) + " - " + str(audio["TIT2"]) + " --- " + str(duration) +"sec")
				all_duration = all_duration + duration
	return "{0}min ({1}sec)".format(round(all_duration/60.0,1), all_duration)

# playlist
def get_info3(client, ip):
	t.download_script(client, "/home/pi/scripts/kr_ritail_1.sh", "./tmp/kr_ritail_1_" + ip +".txt")
	time.sleep(5)
	out = ""
	with open("./tmp/kr_ritail_1_" + ip + ".txt") as f:
		for line in f:
			if line[0] is "#":
				continue
			l = line.split(" ")
			if len(l) > 3:
				path = l[3]
				track = path.split("/")[4]
				out = out + track + "\n"
	return "List of track: '\n' {0}".format(out)
