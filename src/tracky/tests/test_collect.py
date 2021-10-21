from tracky.data_types import getMyCollection
from tracky.tracker import get_tracker
from util.args import get_arg_parser
import json
import pytest
from programs import program1
from os.path import exists


def collect(config):
    args = get_arg_parser(config)
    f = open(args.jsoninputpath)
    user = json.load(f)
    myUser = getMyCollection(user, args)
    program1.main(myUser)

    tracker = get_tracker()

    # Assertions
    filename = f'program1_{tracker.timestamp}.jsonl'
    assert tracker.mode == 'collect'
    assert exists(f'{tracker.output_directory}{filename}')


def test():
    test_configs = [
        [
            "collect",
            "--jsoninputpath",
            "./data/objects/good.json",
            "--outputdirectory",
            "./output/tests/"
        ]
    ]
    for config in test_configs:
        collect(config)


if __name__ == "__main__":
    test()
