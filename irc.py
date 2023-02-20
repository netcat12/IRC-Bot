import socket
import sys
import time

class IRC:
    def __init__(self, server, port, channel, botnick):
        self.server = server
        self.port = port
        self.channel = channel
        self.botnick = botnick
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        print("\033[93mConnecting to {}...\033[0m".format(self.server))
        self.irc.connect((self.server, self.port))
        print("\033[92mConnected to {}!\033[0m".format(self.server))

    def join_channel(self):
        print("\033[93mJoining channel {}...\033[0m".format(self.channel))
        self.irc.send(bytes("JOIN " + self.channel + "\n", "UTF-8"))
        print("\033[92mJoined channel {}!\033[0m".format(self.channel))

    def send_message(self, message):
        print("\033[93mSending message: {}\033[0m".format(message))
        self.irc.send(bytes("PRIVMSG " + self.channel + " :" + message + "\n", "UTF-8"))
        print("\033[92mMessage sent!\033[0m")

    def listen(self):
        print("\033[93mListening for messages...\033[0m")
        while True:
            data = self.irc.recv(4096)
            if data:
                message = data.decode("UTF-8")
                print("\033[94m{}\033[0m".format(message.strip()))
                if "PING" in message:
                    self.irc.send(bytes("PONG " + message.split()[1] + "\r\n", "UTF-8"))

if __name__ == "__main__":
    server = input("\033[96mEnter the IRC server: \033[0m")
    port = input("\033[96mEnter the port number: \033[0m")
    channel = input("\033[96mEnter the channel: \033[0m")
    botnick = input("\033[96mEnter the bot nickname: \033[0m")
    irc = IRC(server, int(port), channel, botnick)
    irc.connect()
    irc.join_channel()
    irc.send_message("Hello, world!")
    print("\033[93mLoading...\033[0m")
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write("\033[96m.\033[0m")
        sys.stdout.flush()
    print("\n\033[92mDone!\033[0m")
    irc.listen()
