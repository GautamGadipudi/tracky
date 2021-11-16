import json
from util.args import get_arg_parser
from tracky.data_types import getMyCollection


def init_program(config):
    args = get_arg_parser(config)
    f = open(args.jsoninputpath)
    user = json.load(f)
    myUser = getMyCollection(user, args)
    return myUser
