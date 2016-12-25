#!/usr/bin/python3.5

# https://github.com/phil294/Tagesschau-Teaser

from pyquery import PyQuery
import urllib
import tkinter.messagebox as msgbox
import webbrowser
import os.path

FILE_LASTTEASER = 'last.dat'

def fltr():
	text = PyQuery(this).text()
	if 'rdensprache' in text:
		return False
	if 'vor 20 Jahren' in text:
		return False
	return True
	
url = 'http://www.tagesschau.de/multimedia/sendung/index.html'

request = urllib.request.Request(url)
opener = urllib.request.build_opener()
html = opener.open(request).read().decode('utf-8')

jquery = PyQuery(html)
ahs = jquery.find("div.teaser:contains('tagesschau')").filter(fltr).find('.teasertext a')
if len(ahs) < 1:
	msgbox.showwarning('TAGESSCHAU', 'Could not get div.teaser:contains("tagesschau"). Exiting.')
	exit()
a = PyQuery(ahs[0])
teaser = a.text() #.encode('utf-8')
href = 'http://tagesschau.de' + a.attr('href')

lastTeaser = ""
if os.path.isfile(FILE_LASTTEASER):
	f = open(FILE_LASTTEASER, 'r')
	lastTeaser = f.read()
	f.close()
f = open(FILE_LASTTEASER, 'w')
f.write(teaser)
f.close()

if lastTeaser == teaser:
	print('gleiche tagesschau wie beim letzten check.')
	exit()

teaser = teaser.replace(',', '\n\n')	
resp = msgbox.askquestion("TAGESSCHAU", teaser, icon='info')
if resp == 'yes':
	webbrowser.open(href)