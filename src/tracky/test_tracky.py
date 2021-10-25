from tracky.data_types import getMyCollection
from tracky.tracker import get_tracker
from util.args import get_arg_parser
import json
import pytest
from programs import program1
import os
from os.path import exists



def init(config):
    args = get_arg_parser(config)
    f = open(args.jsoninputpath)
    user = json.load(f)
    myUser = getMyCollection(user, args)
    return myUser


def test_match_bad(config=[
    "match",
    "--jsoninputpath",
    "./data/objects/bad.json",
    "--targetfile",
    "./output/eval/good.jsonl"
]):

    test_collect_good()
    myUser = init(config)
    with pytest.raises(Exception) as e:
        program1.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'match'
    # assert pytest.raises(Exception)
    assert tracker.frame_id == 0


def test_match_good(config=[
    "match",
    "--jsoninputpath",
    "./data/objects/good.json",
    "--targetfile",
    "./output/eval/good.jsonl"
]):

    test_collect_good()
    myUser = init(config)
    program1.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'match'
    assert tracker.frame_id == 2


def test_collect_good(config=[
    "collect",
    "--jsoninputpath",
    "./data/objects/good.json",
    "--outputdirectory",
    "./output/eval/"
]):
    myUser = init(config)
    program1.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'collect'
    assert exists(f'{tracker.output_filename}')

    # Move the good data to eval to be used when matching
    try:
        new_filename = f'good.jsonl'
        os.rename(f'{tracker.output_filename}', f'{tracker.output_directory}{new_filename}')
        assert exists(f'{tracker.output_directory}{new_filename}')
    except OSError: 
        pass

    
