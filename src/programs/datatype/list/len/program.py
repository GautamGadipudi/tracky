import sys

from util.setup import init_program


def main(myUser):
    # Expects "some_list" to be of type list
    # Operation (__len__)
    list_count = len(myUser['some_list'])

    print(list_count)

def init(config):
    myUser = init_program(config)
    main(myUser)


if __name__ == "__main__":
    init(sys.argv[1:])
