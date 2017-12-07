import facebook

class Fbfuncs():
    atoken = "EAACEdEose0cBAEFDZAjb4n7iyv3CFQZAMDYTiWAZCaHugu5V60TSzg3efD8c2ZBeiOGZCrdmSSjws4JZAGEIOZA37uZB3ftFRbihUMIMBlcmYJjwzNwErGmyaSEkLIZAldYsEKCYiu9ZCw31gdnNalXNu46As9lWmDFmhUKOeWLkgdOiF7phGsPNsULHyZCe3uZCjRpglxw0wJaSHQZDZD"
    graph = facebook.GraphAPI(access_token = atoken, version = "2.1")
    def update(self, msg):
        self.graph.put_object(parent_object='me', connection_name='feed', message=msg)
