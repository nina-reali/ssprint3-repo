import json

class WriterJson:

    def __init__(self, tweets):
        self.tweets = tweets

    def write(self):
        with open("../tweets.json", 'w') as j:
            json.dump(self.tweets, j, ensure_ascii=False, indent=4)