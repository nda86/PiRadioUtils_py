#!/usr/bin/env bash
old_IFS=$IFS
IFS=$'\n'
all_time=0
for line in $(cat /home/pi/scripts/kr_ritail_1.sh | grep -v "#" | grep mpg321); do
	path=$(echo $line | awk -F " " '{print $4}')
	time_m=$(mpg321 -t $path 2>&1 | grep Decoding | awk -F " " '{print$1}' | sed 's/\(\[\|\]\)//g' | awk -F ":" '{print$1}')
	time_s=$(mpg321 -t $path 2>&1 | grep Decoding | awk -F " " '{print$1}' | sed 's/\(\[\|\]\)//g' | awk -F ":" '{print$2}')
	if [[ $time_m -gt 0 ]]; then time_s=$(($time_s*$time_m)); fi
	all_time=$(($all_time+$time_s))
done
min=$(echo "scale=2; $all_time/60" | bc)
echo "All time is: $all_time sec $min min" 
IFS=$old_IFS