import sys

from util.setup import init_program


def main(myUser):
    myUser['some_dict'].clear()


def init(config):
    myUser = init_program(config)
    main(myUser)

if __name__ == "__main__":
    init(sys.argv[1:])
