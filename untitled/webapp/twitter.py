from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API


class Twfuncs():
    ckey = 'buamuduVuPfbdxfYcAKN0YSP0'
    csecret = 'X1SexNg2uv0aXSZ5yOxCSlZEkWj6M5cURrhqRDubHN7Lk7gKtE'
    atoken = '935095787964465152-BDqHf3JXl2s8K3HJybYcnSU2CfWGgWu'
    asecret = 'Afo6iiv05A2KjiclbvDqpihUPfc5wltD6vumeumiUHMr9'
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = API(auth)


    def update(self, message):
        self.api.update_status(message)


