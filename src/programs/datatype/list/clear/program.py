import sys

from util.setup import init_program


def main(myUser):
    # Expects "some_list" to be of type list
    myUser['some_list'].clear()


if __name__ == "__main__":
    myUser = init_program(sys.argv[1:])
    main(myUser)
