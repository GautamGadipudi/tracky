import sys

from util.setup import init_program


def main(myUser):
    # Operation (__len__)
    str_count = len(myUser['some_str'])

    print(str_count)


if __name__ == "__main__":
    myUser = init_program(sys.argv[1:])
    main(myUser)
