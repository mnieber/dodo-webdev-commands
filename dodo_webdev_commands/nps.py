import argparse
from argparse import ArgumentParser

from dodo_commands import CommandError, Dodo, remove_trailing_dashes


def _args():
    parser = ArgumentParser(description='Runs nps')
    parser.add_argument('nps_args', nargs=argparse.REMAINDER)

    args = Dodo.parse_args(parser)
    args.cwd = Dodo.get_config('/NODE/cwd')
    args.nps = Dodo.get_config('/NODE/nps', 'nps')

    # Raise an error if something is not right
    if False:
        raise CommandError('Oops')

    return args


# Use safe=False if the script makes changes other than through Dodo.run
if Dodo.is_main(__name__, safe=True):
    args = _args()

    Dodo.run([args.nps, *remove_trailing_dashes(args.nps_args)], cwd=args.cwd)
