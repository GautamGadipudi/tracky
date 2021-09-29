import sys
import json
import os

from tracky.data_types import getMyCollection, Tracker


def main():
    fname = sys.argv[1]
    f = open(fname)
    users = json.load(f)

    user = getMyCollection(users)

    # Program logic / operations
    try:
        name = user['name']
        freinds = user['friends']
        friend_count = len(user['friends'])

        for friend in user['friends']:
            print(f"{friend}\n")

        print(f"{name} has {friend_count} friends.")
    except Exception as e:
        print(e)
    finally:
        Tracker.dump(
            "./output/", f"program1_{os.path.basename(fname).split('.')[0]}")


if __name__ == "__main__":
    main()
