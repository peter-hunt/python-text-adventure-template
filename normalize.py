# this module is not necessary, or can be git-ignored

def normalize():
    with open('path-to-assets-or-data') as file:
        content = file.read()

    with open('path-to-assets-or-data', 'w') as file:
        file.write('organized content')


if __name__ == '__main__':
    normalize()
