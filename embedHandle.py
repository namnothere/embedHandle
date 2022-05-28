from flask import Flask, render_template, request
from tiktokHandle import TikTokHandle
from databaseHandle import Database
from threading import Thread
import urllib.parse
import os
db = Database()
tk = TikTokHandle()

app = Flask(__name__)

BASE_URL = os.getenv("BASE_URL")

def oEmbedGen(description, video_link):
	out = {
		"provider_name" : "nem",
		"provider_url"  : "https://youtu.be/dQw4w9WgXcQ",
		# "title"         : description,
		"author_name"   : description,
		"author_url"    : video_link
		}
	return out

def oEmbedURLrender(description, video_link):
	safe_query = urllib.parse.quote_plus(description)
	url = f"{BASE_URL}/oembed.json?desc={safe_query}&link={video_link}"
	return url


@app.route('/')
def home():
	return "baerysotp", 200



@app.route("/<videoID>")
def renderEmbed(videoID):
	video = db.getVideo(videoID)
	cover = video['cover']
	Id = video['username']
	nickName = video['screenName']
	desc = video['desc']
	width = video['width']
	height = video['height']
	appname = "NoBaePleaseDontUseTikTok"
	video_url = video['video_url']
	url = oEmbedURLrender(desc, video_url)
	return render_template('index.html', cover = cover, Id = Id, nickname = nickName, desc = desc, width = width, height = height, video_url = video_url, appname = appname, embed=url)

@app.route('/oembed.json') #oEmbed endpoint
def oembedend():
	desc  = request.args.get("desc", None)
	link  = request.args.get("link", None)
	return  oEmbedGen(desc, link)

def run():
	app.run()

def run_threaded():
	Thread(target=run).start()


if __name__ == '__main__':
	run_threaded()