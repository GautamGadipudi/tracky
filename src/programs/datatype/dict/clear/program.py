import sys

from util.setup import init_program


def main(myUser):
    myUser['some_dict'].clear()


if __name__ == "__main__":
    myUser = init_program(sys.argv[1:])
    main(myUser)
