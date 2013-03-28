zcat -f /var/log/nginx/tinkov-audio* | /usr/local/bin/goaccess -a > audio.html
zcat -f /var/log/nginx/tinkov-rss* | /usr/local/bin/goaccess -a > rss.html
zcat -f /var/log/nginx/tinkov-access* | /usr/local/bin/goaccess -a > all.html

