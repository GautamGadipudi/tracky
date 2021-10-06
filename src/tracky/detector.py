import argparse
import textwrap

from programs import program1
import json


def main():
    parser = get_arg_parser()
    args = parser.parse_args()

    if args.mode == 'collect':
        program1.main(args.jsoninputpath)
    elif args.mode == 'match':
        eval_traces = get_traces(args.evaluationfile)
        target_traces = get_traces(args.targetfile)

        is_match = match_traces(eval_traces, target_traces)
        print(is_match)


def get_traces(filename):
    traces = []
    lines = []
    with open(filename, mode='r') as f:
        lines = f.readlines()

    traces = [json.loads(line) for line in lines]
    return traces


def match_traces(traces: list, target_traces: list):
    return traces == target_traces


def get_arg_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Silent JSON detector
            ----------------------------
            Mode 1: Collect frame information of operations performed on JSON data.

            Mode 2: Match collected frame information against data collected from new JSON data.
            '''
                                    )
    )

    subparsers = parser.add_subparsers(dest='mode')

    parser_collect = subparsers.add_parser('collect')
    parser_collect.add_argument('--jsoninputpath', required=True, type=str)

    parser_match = subparsers.add_parser('match')
    parser_match.add_argument('--evaluationfile', required=True, type=str)
    parser_match.add_argument('--targetfile', required=True, type=str)

    return parser


if __name__ == "__main__":
    main()
