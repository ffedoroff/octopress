# sudo apt-get install ffmpeg libavcodec-extra-53
rm -f tmp.sh
for f in *.m4a
	do 
	echo "rm -f t.mp3" >> tmp.sh
	echo "avconv -i "\"$f\"" -map_metadata 0:s:0 -metadata comment=\"http://tinkov.linkentools.com/\" -b 80k -ac 1 t.mp3" >> tmp.sh
	echo "vbrfix -always t.mp3 "\"${f%.m4a}.mp3\""" >> tmp.sh
	echo "rm t.mp3" >> tmp.sh
done
echo "rm -f vbrfix* tmp.sh" >> tmp.sh
#bash tmp.sh
#echo "now run: bash tmp.sh"
