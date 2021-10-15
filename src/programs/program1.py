import sys
import json

from tracky.data_types import getMyCollection


def main(jsoninputpath: str):
    f = open(jsoninputpath)
    user = json.load(f)

    myUser = getMyCollection(user)

    # Operation 1 (__len__)
    friend_count = len(myUser['friends'])

    # Operation 2 (__iter__)
    for friend in myUser['friends']:
        print(friend)


if __name__ == "__main__":
    main()
