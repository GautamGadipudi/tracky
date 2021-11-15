import sys
import json

from tracky.data_types import getMyCollection
from util.args import get_arg_parser

def init():
    args = get_arg_parser(sys.argv[1:])
    f = open(args.jsoninputpath)
    user = json.load(f)

    myUser = getMyCollection(user, args)
    main(myUser)

def main(myUser):
    # expects "friends" attribute to be of type myList

    # Operation (__len__)
    list_count = len(myUser['some_list'])

    print(list_count)


if __name__ == "__main__":
    init()
