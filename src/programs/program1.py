import sys
import json

from tracky.data_types import getMyCollection
from util.args import get_arg_parser

def init():
    parser = get_arg_parser()
    args = parser.parse_args()
    f = open(args.jsoninputpath)
    user = json.load(f)

    myUser = getMyCollection(user, args)
    main(myUser)

def main(myUser):
    # Operation 1 (__len__)
    friend_count = len(myUser['friends'])

    # Operation 2 (__iter__)
    for friend in myUser['friends']:
        print(friend)


if __name__ == "__main__":
    init()
