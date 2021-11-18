import os
from os.path import exists
import pytest

import programs.datatype.list.len.program as p1
import programs.datatype.list.iter.program as p2
import programs.datatype.list.clear.program as p3

from tracky.tracker import get_tracker
from util.setup import init_program

data_dir = "./data/programs/list"
output_dir = "./output/programs/list"


configs = {
    "p1": {
        "program": p1,
        "collect": {
            "good": [
                "collect",
                "--jsoninputpath",
                f"{data_dir}/len/good.json",
                "--outputdirectory",
                f"{output_dir}/len/"
            ]
        },
        "match": {
            "good": [
                "match",
                "--jsoninputpath",
                f"{data_dir}/len/good.json",
                "--targetfile",
                f"{output_dir}/len/good.jsonl"
            ],
            "bad1": [
                "match",
                "--jsoninputpath",
                f"{data_dir}/len/bad1.json",
                "--targetfile",
                f"{output_dir}/len/good.jsonl"
            ],
            "bad2": [
                "match",
                "--jsoninputpath",
                f"{data_dir}/len/bad2.json",
                "--targetfile",
                f"{output_dir}/len/good.jsonl"
            ]
        }
    },
    "p2": {
        "program": p2,
        "collect": {
            "good": [
                "collect",
                "--jsoninputpath",
                f"{data_dir}/iter/good.json",
                "--outputdirectory",
                f"{output_dir}/iter/"
            ]
        },
        "match": {
            "good": [
                "match",
                "--jsoninputpath",
                f"{data_dir}/iter/good.json",
                "--targetfile",
                f"{output_dir}/iter/good.jsonl"
            ],
            "bad1": [
                "match",
                "--jsoninputpath",
                f"{data_dir}/iter/bad1.json",
                "--targetfile",
                f"{output_dir}/iter/good.jsonl"
            ],
            "bad2": [
                "match",
                "--jsoninputpath",
                f"{data_dir}/iter/bad2.json",
                "--targetfile",
                f"{output_dir}/iter/good.jsonl"
            ]
        }
    },
    "p3": {
        "program": p3,
        "collect": {
            "good": [
                "collect",
                "--jsoninputpath",
                f"{data_dir}/clear/good.json",
                "--outputdirectory",
                f"{output_dir}/clear/"
            ]
        },
        "match": {
            "good": [
                "match",
                "--jsoninputpath",
                f"{data_dir}/clear/good.json",
                "--targetfile",
                f"{output_dir}/clear/good.jsonl"
            ],
            "bad1": [
                "match",
                "--jsoninputpath",
                f"{data_dir}/clear/bad1.json",
                "--targetfile",
                f"{output_dir}/clear/good.jsonl"
            ]
        }
    }
}


@pytest.mark.parametrize(
    "config,program",
    [
        (configs["p1"]['collect']['good'], p1),
        (configs["p2"]['collect']['good'], p2),
        (configs["p3"]['collect']['good'], p3),
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
        (configs["p3"]['match']['bad1'], p3),
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
        (configs["p3"]['match']['good'], p3),
    ]
)
def test_match_good(config, program):

    myUser = init_program(config)
    program.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'match'
