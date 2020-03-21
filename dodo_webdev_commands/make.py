from argparse import ArgumentParser

from dodo_commands import CommandError, Dodo


def _args():
    parser = ArgumentParser(description='Runs make')

    parser.add_argument('what')

    args = Dodo.parse_args(parser)
    args.cwd = Dodo.get_config('/MAKE/src_dir')

    # Raise an error if something is not right
    if False:
        raise CommandError('Oops')

    return args


# Use safe=False if the script makes changes other than through Dodo.run
if Dodo.is_main(__name__, safe=True):
    args = _args()

    Dodo.run(['make', args.what], cwd=args.cwd)
