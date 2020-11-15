class Game:
    def __init__(self):
        self.save()

    def save(self):
        content = 'dumped self'

        with open('path-to-data', 'w') as file:
            file.write(content)

    @classmethod
    def load(cls, game_name):
        with open('path-to-data') as file:
            content = file.read()

        if not cls.is_valid('parsed content'):
            print('Invalid game data')
            return  # or raise an exception

        return cls()

    @staticmethod
    def is_valid(data, alert=True):
        if not 'condition':
            if alert:
                print('Error message')
            return False

        # pass the alert variable to 'is_valid' recursion if it exists

        return True

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
