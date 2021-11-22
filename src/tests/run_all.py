import glob
import os
from os.path import exists
import importlib
import pytest

from tracky.tracker import get_tracker
from util.setup import init_program

PROGRAMS_DIR = "./src/programs/datatype/"
DATA_DIR = "./data/programs/"
OUTPUT_DIR = "./output/programs/"

good_files_matcher = "good*.json"
bad_files_matcher = "bad*.json"
target_filename = "good.jsonl"

print(os.getcwd())

def do():
    for datatype in os.listdir(PROGRAMS_DIR):
        if datatype == '__init__.py' or datatype == "__pycache__":
            continue

        for method in os.listdir(f"{PROGRAMS_DIR}{datatype}/"):
            if method == '__init__.py' or method == "__pycache__":
                continue

            program = importlib.import_module(
                f"programs.datatype.{datatype}.{method}.program")

            good_data_files = glob.glob(
                f"{DATA_DIR}{datatype}/{method}/{good_files_matcher}")
            bad_data_files = glob.glob(
                f"{DATA_DIR}{datatype}/{method}/{bad_files_matcher}")

            target_file = glob.glob(
                f"{OUTPUT_DIR}{datatype}/{method}/{target_filename}")[0]

            run_scenarios(program, good_data_files, bad_data_files, target_file,
                f"{OUTPUT_DIR}{datatype}/{method}/")


def run_scenarios(program, good_data_files, bad_data_files, target_file, output_dir):
    # test collect good data
    for path in good_data_files:
        collect_good([
            "collect",
            "--jsoninputpath",
            path,
            "--outputdirectory",
            output_dir
        ], program)

    # test match good good
    for path in good_data_files:
        match_good([
            "match",
            "--jsoninputpath",
            path,
            "--targetfile",
            f"{target_file}"
        ], program)

    # test match bad good
    for path in bad_data_files:
        match_bad([
            "match",
            "--jsoninputpath",
            path,
            "--targetfile",
            f"{target_file}"
        ], program)


def collect_good(config, program):
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


def match_bad(config, program):
    myUser = init_program(config)
    with pytest.raises(Exception) as e:
        program.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'match'


def match_good(config, program):
    myUser = init_program(config)
    program.main(myUser)

    tracker = get_tracker()

    # Assertions
    assert tracker.mode == 'match'


if __name__ == "__main__":
    do()
