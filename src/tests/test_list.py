import os
from os.path import exists
import pytest

import programs.datatype.list.len.program as p1
import programs.datatype.list.iter.program as p2

from tracky.tracker import get_tracker
from util.setup import init_program


configs = {
    "p1": {
        "collect": {
            "good": [
                "collect",
                "--jsoninputpath",
                "./data/programs/list/len/good.json",
                "--outputdirectory",
                "./output/programs/list/len/"
            ]
        },
        "match": {
            "good": [
                "match",
                "--jsoninputpath",
                "./data/programs/list/len/good.json",
                "--targetfile",
                "./output/programs/list/len/good.jsonl"
            ],
            "bad1": [
                "match",
                "--jsoninputpath",
                "./data/programs/list/len/bad1.json",
                "--targetfile",
                "./output/programs/list/len/good.jsonl"
            ],
            "bad2": [
                "match",
                "--jsoninputpath",
                "./data/programs/list/len/bad2.json",
                "--targetfile",
                "./output/programs/list/len/good.jsonl"
            ]
        }
    },
    "p2": {
        "collect": {
            "good": [
                "collect",
                "--jsoninputpath",
                "./data/programs/list/iter/good.json",
                "--outputdirectory",
                "./output/programs/list/iter/"
            ]
        },
        "match": {
            "good": [
                "match",
                "--jsoninputpath",
                "./data/programs/list/iter/good.json",
                "--targetfile",
                "./output/programs/list/iter/good.jsonl"
            ],
            "bad1": [
                "match",
                "--jsoninputpath",
                "./data/programs/list/iter/bad1.json",
                "--targetfile",
                "./output/programs/list/iter/good.jsonl"
            ],
            "bad2": [
                "match",
                "--jsoninputpath",
                "./data/programs/list/iter/bad2.json",
                "--targetfile",
                "./output/programs/list/iter/good.jsonl"
            ]
        }
    }
}


@pytest.mark.parametrize(
    "config,program",
    [
        (configs["p1"]['collect']['good'], p1),
        (configs["p2"]['collect']['good'], p2)
    ]
)
def test_collect_good(config, program):
    myUser = init_program(config)
    program.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'collect'
    assert exists(f'{tracker.output_filename}')

    # Move the good data to eval to be used when matching
    try:
        new_filename = f'good.jsonl'
        os.rename(f'{tracker.output_filename}',
                  f'{tracker.output_directory}{new_filename}')
        assert os.path.exists(f'{tracker.output_directory}{new_filename}')
    except OSError:
        pass


@pytest.mark.parametrize(
    "config,program",
    [
        (configs["p1"]['match']['bad1'], p1),
        (configs["p1"]['match']['bad2'], p1),
        (configs["p2"]['match']['bad1'], p2),
        (configs["p2"]['match']['bad2'], p2),
    ]
)
def test_match_bad(config, program):

    myUser = init_program(config)
    with pytest.raises(Exception) as e:
        program.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'match'


@pytest.mark.parametrize(
    "config,program",
    [
        (configs["p1"]['match']['good'], p1),
        (configs["p2"]['match']['good'], p2),
    ]
)
def test_match_good(config, program):

    myUser = init_program(config)
    program.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'match'
