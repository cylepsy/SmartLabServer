from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API


class Twfuncs():
    ckey = 'buamuduVuPfbdxfYcAKN0YSP0'
    csecret = 'X1SexNg2uv0aXSZ5yOxCSlZEkWj6M5cURrhqRDubHN7Lk7gKtE'
    atoken = '935095787964465152-BDqHf3JXl2s8K3HJybYcnSU2CfWGgWu'
    asecret = 'Afo6iiv05A2KjiclbvDqpihUPfc5wltD6vumeumiUHMr9'
    # this is the backup account for twitter
    ckey2 = 'BYVm95A9v6ujDhtVF0M4RwYok'
    csecret2 = 'QItEPZdWGErMSnJs0Fk8LuDYNBmYTqyemooPSyv8fhA5P3ob9y'
    atoken2 = '938444061580709893-CAGfIZdU4jEAovYxE9KiZa1yWsckQ8g'
    asecret2 = 'E1hiKsMFdu7vxu8XUiAKIRe2YO3NeTyj0SybzvDp6tejR'
    auth = OAuthHandler(ckey2, csecret2)
    auth.set_access_token(atoken2, asecret2)
    api = API(auth)


    def update(self, message):
        self.api.update_status(message)
