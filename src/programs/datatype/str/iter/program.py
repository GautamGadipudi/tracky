import sys

from util.setup import init_program


def main(myUser):
    # Operation (__iter__)
    for c in myUser['some_str']:
        print(c)

def init(config):
    myUser = init_program(config)
    main(myUser)


if __name__ == "__main__":
    init(sys.argv[1:])