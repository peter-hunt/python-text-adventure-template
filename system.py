class System:
    def __init__(self):
        pass

    def create(self):
        pass

    def launch(self, game_name):
        pass

    def loop(self):
        while True:
            cmd = input('> ')
            if cmd == 'exit':
                return

    def run(self):
        try:
            self.loop()
        except KeyboardInterrupt:
            pass
