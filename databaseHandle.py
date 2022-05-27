import pymongo
import time
import os
from dotenv import load_dotenv

load_dotenv()

DBclient = os.getenv("CLIENT")

class Database():
    def __init__(self):
        self.client = None
        self.connected = False

    def connectDB(self):
        if not self.connected:
            try:
                self.client = pymongo.MongoClient(DBclient, serverSelectionTimeoutMS=3000)
                self.connected = True
            except Exception as e:
                print("connectDB [Error]: " + str(e))
                time.sleep(10)
                return self.connectDB()

    def getVideo(self, id):
        self.connectDB()
        db = self.client.TikTok.bae.find_one({'id':'tiktok'})
        return db['videos'][str(id)]
