import sys

from util.setup import init_program


def main(myUser):
    # Operation (__iter__)
    # Expects "some_list" to be of type list
    for k in myUser['some_dict']:
        print(k)
        
def init(config):
    myUser = init_program(config)
    main(myUser)


if __name__ == "__main__":
    init(sys.argv[1:])
