#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mutagen.mp3 import MP3

with open("/home/pi/scripts/kr_ritail_1.sh") as f:
	all_duration = 0
	for line in f:
		if line[0] is "#":
			continue
		l = line.split(" ")
		if len(l) > 3:
			path = l[3]
			audio = MP3(path)
			duration = round(audio.info.length)
			print(str(audio["TPE1"]) + " - " + str(audio["TIT2"]) + " --- " + str(duration) +"sec")
			all_duration = all_duration + duration
	print("All time is: %.1fmin (%isec)" % (round(all_duration/60.0,1), all_duration))

