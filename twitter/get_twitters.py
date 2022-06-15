from credentials_twitter import CredentialsTwitter
import tweepy as tw

class GetTwitters:

    def __init__(self):
        credentials = CredentialsTwitter()
        self.auth = tw.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
        self.api = tw.API(self.auth, wait_on_rate_limit=True, timeout=200)

    def get(self, search_query):
        tweets = []
        for query in search_query:
            tweets = tw.Cursor(self.api.search_tweets, q=query, lang="pt").items(1000)

            for tweet in tweets:
                if 'pix' in tweet.text:
                    linha= [tweet.id,str(tweet.user.name).rstrip('\n').replace('"',""),str(tweet.created_at).rstrip('\n'),tweet.text]
                    tweets.append(linha)

        return tweets