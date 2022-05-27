from TiktokApi import *

class TikTokHandle():
    def __init__(self, username = None) -> None:
        self.api = Tiktok()
        self.username = username


    def getUser(self):
        try:
            self.user = self.api.getUserFeed(self.username)[0]
            return self.user
        except Exception as e:
            print("getUser [Error]: " + str(e))
            return "getUser [Error]: " + str(e)
