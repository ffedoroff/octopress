# sudo apt-get install ffmpeg libavcodec-extra-53
rm -f tmp.sh
for f in *.mp4
        do 
        echo "avconv -i "\"$f\"" -vn -acodec copy "\"${f%.mp4}.m4a\"""  >> tmp.sh
done
#bash tmp.sh
echo "now run: bash tmp.sh"
