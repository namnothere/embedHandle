from flask import Flask, render_template, request
from tiktokHandle import TikTokHandle
from databaseHandle import Database
from threading import Thread
import urllib.parse
import os
db = Database()
tk = TikTokHandle()

app = Flask(__name__)

TIKTOK_URL = "https://www.tiktok.com/@"

BASE_URL = os.getenv("BASE_URL")

def oEmbedGen(description, video_link):
	out = {
		"provider_name" : "nem",
		"provider_url"  : "https://youtu.be/dQw4w9WgXcQ",
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



@app.route("/<username>/<videoID>")
def renderEmbed(username, videoID):
	video = db.getVideo(username, videoID)
	cover = video['cover']
	Id = video['username']
	nickName = video['screenName']
	desc = video['desc']
	width = video['width']
	height = video['height']
	appname = "NoBaePleaseDontUseTikTok"
	video_url = video['video_url']
	orLink = f"{TIKTOK_URL}{username}/video/{videoID}"
	url = oEmbedURLrender(desc, video_url)
	return render_template('index.html', cover = cover, Id = Id, nickname = nickName, desc = desc, width = width, height = height, video_url = video_url, appname = appname, embed=url, orLink = orLink)

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