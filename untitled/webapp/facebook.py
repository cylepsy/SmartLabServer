import facebook

class Fbfuncs():
    atoken = "EAACEdEose0cBAM68sgQFUpEPBcZBPwTk02jujS0qZA9QiWICSA6EcJumhxdlid4t6KTztZBqACYkJwbj7HALlVgyzSQozDJweU4ba1hYU0RGlhskzsZBcoXWTuOtIm6KJTZC6fzkMTCf7AxtTbzaG04nAh8l2RIlXvZC9abZBpFkxxbUatwaHUjGH4FXnAllHWZCaO7MZBz8qUQZDZD"
    graph = facebook.GraphAPI(access_token = atoken, version = "2.1")
    def update(self, msg):
        self.graph.put_object(parent_object='me', connection_name='feed', message=msg)
