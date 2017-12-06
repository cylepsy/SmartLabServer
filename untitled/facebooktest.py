import facebook

graph = facebook.GraphAPI(access_token = "EAACEdEose0cBABIliQnhKw2X7qpcTw0xC9bt2umLZCEYlJAZA0AjoblX6vxKTzWPWHbkJFLin0OL759OLr2eJDr1l2h0FFEqkBCeBZBL4XkBHAdboOZAsLZB01cPPSiHMxOCLTtPGkouRMTAr6HVfjvAdHnaBqGHwjy3AUZAZCZAb17FRvevjol9Wo5fzPuM6AkZD", version = "2.1")
graph.put_object(parent_object='me', connection_name='feed', message='viktor went kickboxing -from python')
