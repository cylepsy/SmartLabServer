import facebook

class Fbfuncs():
    atoken = "EAACEdEose0cBAFh2DxErANhdlf6JXiq4QpUgABa2q168AtEe9O7Lw17taKyWLx3dKBZBZCdoDXLVcVlbv8SzoZCjiEIHjRYQxSgCXsjpJutarmnpZAZC4Lv557tc4QZB7DIU5x8kJxVpwqduaIbYv89tN2jtA4pjZC2hq4We0OHkXANHZAyCZAqrYNqOKd3NSjRonKNwwSjMhWwZDZD"
    graph = facebook.GraphAPI(access_token = atoken, version = "2.1")
    def update(self, msg):
        self.graph.put_object(parent_object='me', connection_name='feed', message=msg)
