import facebook

class Fbfuncs():
    atoken = "EAACEdEose0cBADqWv0l9sdIGqZApBrOpRLOZAEk3d7XZBK98wZChTRTAP5vRqYOcUWjnpWQV08Owfoe2EoxjSG1kYGvUSZAcPO6zZCFZCJq30rOJ5QIUYWFEXcSKCPOxc2xH2rQdxWotIdkpCeulocn7jZCCwmrQur7iCL4TZBtmRxsMlrhCqWGw1pHg22vr3ZB0FQAzNM2FHeAQZDZD"
    graph = facebook.GraphAPI(access_token = atoken, version = "2.1")
    def update(self, msg):
        self.graph.put_object(parent_object='me', connection_name='feed', message=msg)
