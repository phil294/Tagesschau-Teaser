# Tagesschau-Teaser
Ubuntu: Tagesschau Schlagzeilen downloader + prompt script [PYTHON]

!(preview)[https://i.imgur.com/0ZQtQ34.png]
(Yes = open video in browser)

Meant to be used as a crontab. Crontabs do not have access to the session which is needed for TKinter's alert. Granting display access as root:

sudo crontab -e
	30 * * * * /home/?/bin/tagesschau/tagesschauCronRoot.sh
	
Executes /home/?/bin/tagesschau/tagesschau.py every 30 mins.
