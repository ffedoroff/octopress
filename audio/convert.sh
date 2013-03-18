for f in *.m4a
      do 
      echo ffmpeg -i "\"$f\"" -b 192k "\"${f%.m4a}.mp3\""
done
