from tracky.data_types import getMyCollection
from tracky.tracker import get_tracker
from util.args import get_arg_parser
import json
import pytest
from programs import program1
from os.path import exists

def init(config):
    args = get_arg_parser(config)
    f = open(args.jsoninputpath)
    user = json.load(f)
    myUser = getMyCollection(user, args)
    return myUser

def match_bad():
    
    config = [
            "match",
            "--jsoninputpath",
            "./data/objects/bad.json",
            "--targetfile", 
            "./output/eval/good.jsonl"
        ]
    myUser = init(config)
    with pytest.raises(Exception) as e:
        program1.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'match'
    # assert pytest.raises(Exception)
    assert tracker.frame_id == 0

def match_good():
    config = [
            "match",
            "--jsoninputpath",
            "./data/objects/good.json",
            "--targetfile", 
            "./output/eval/good.jsonl"
        ]
    myUser = init(config)
    program1.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'match'
    assert tracker.frame_id == 0


def test():
    match_good()
    match_bad()

if __name__ == "__main__":
    test()