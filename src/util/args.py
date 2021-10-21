import argparse
import textwrap

def get_arg_parser(args):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            RIT Capstone Project (2211)

            Title: Detecting silent JSON changes in dynamic programming languages
            Author: Gautam Gadipudi
            Advisor: Dr. Michael Mior
            _____________________________________________________________________ 
        '''),
        epilog=textwrap.dedent('''\
            Rochester Institute of Technology
            All rights reserved.
        '''
        )
    )

    subparsers = parser.add_subparsers(dest='mode')

    parser_collect = subparsers.add_parser('collect')
    parser_collect.add_argument('--jsoninputpath', '-i', required=True, type=str)
    parser_collect.add_argument('--outputdirectory', '-o', type=str, dest='outputdirectory')
    parser_collect.add_argument('--verbose', '-v', dest='verbose', action='store_true')

    parser_match = subparsers.add_parser('match')
    parser_match.add_argument('--jsoninputpath', '-i', required=True, type=str)
    parser_match.add_argument('--targetfile', '-t', required=True, type=str)
    parser_match.add_argument('--verbose', '-v', dest='verbose', action='store_true')


    return parser.parse_args(args)