import sys

from util.setup import init_program


def main(myUser):
    # Operation (__len__)
    str_count = len(myUser['some_str'])

    print(str_count)

def init(config):
    myUser = init_program(config)
    main(myUser)


if __name__ == "__main__":
    init(sys.argv[1:])
