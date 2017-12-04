import socket


class Light():
    def __init__(self):

        s = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

        server_address = ('78.62.58.245', 38899)
        s.connect(server_address)

        prefix = 'APP#AC:CF:23:28:C0:20#CMD#'

        def lightOn(self, zone):
            if zone == 3:
                self.s.send(self.prefix + '490\n')
                self.s.send(self.prefix + 'c90\n')

            if zone == 2:
                self.s.send(self.prefix + '470\n')
                self.s.send(self.prefix + 'c70\n')

            if zone == 1:
                self.s.send(self.prefix + '450\n')
                self.s.send(self.prefix + 'c50\n')

        def lightOff(self, zone):
            if zone == 3:
                self.s.send(self.prefix + '4a0\n')

            if zone == 2:
                self.s.send(self.prefix + '480\n')

            if zone == 1:
                self.s.send(self.prefix + '460\n')

        def allOn(self):
            self.s.send(self.prefix + '420\n')

        def allOff(self):
            self.s.send(self.prefix + '410\n')