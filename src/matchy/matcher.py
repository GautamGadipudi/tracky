import argparse
import textwrap

from programs import program1
import os


def main():
    parser = get_arg_parser()
    args = parser.parse_args()

    if args.mode == 'collect':
        program1.main(args.jsoninputpath)
    elif args.mode == 'match':
        program1.main(args.jsoninputpath)
        print(args.jsoninputpath)
        print(args.evaluationfile)

def get_arg_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Tracky
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
    parser_match.add_argument('--jsoninputpath', required=True, type=str)
    parser_match.add_argument('--evaluationfile', required=True, type=str)

    return parser


if __name__ == "__main__":
    main()


'''
python3 matcher.py 
'''
