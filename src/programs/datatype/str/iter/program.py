import sys

from util.setup import init_program


def main(myUser):
    # Operation (__iter__)
    for c in myUser['some_str']:
        print(c)


if __name__ == "__main__":
    myUser = init_program(sys.argv[1:])
    main(myUser)
