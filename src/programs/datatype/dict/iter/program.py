import sys

from util.setup import init_program


def main(myUser):
    # Operation (__iter__)
    # Expects "some_list" to be of type list
    for k in myUser['some_dict']:
        print(k)


if __name__ == "__main__":
    myUser = init_program(sys.argv[1:])
    main(myUser)
