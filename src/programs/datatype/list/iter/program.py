import sys

from util.setup import init_program


def main(myUser):
    # Operation (__iter__)
    # Expects "some_list" to be of type list
    for friend in myUser['some_list']:
        print(friend)


if __name__ == "__main__":
    myUser = init_program(sys.argv[1:])
    main(myUser)
