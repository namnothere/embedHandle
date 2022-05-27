from flask import Flask, render_template
from tiktokHandle import TikTokHandle
from databaseHandle import Database
from threading import Thread
db = Database()
tk = TikTokHandle()

app = Flask(__name__)

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
	return render_template('index.html', cover = cover, Id = Id, nickname = nickName, desc = desc, width = width, height = height, video_url = video_url, appname = appname)



def run():
	app.run()

def run_threaded():
	Thread(target=run).start()


if __name__ == '__main__':
	run_threaded()