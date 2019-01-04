from argparse import ArgumentParser
from dodo_commands.framework import Dodo
import os


def _args():
    parser = ArgumentParser()
    args = Dodo.parse_args(parser)
    args.node_modules_dir = Dodo.get_config('/SERVER/node_modules_dir')
    args.pip = os.path.join(Dodo.get_config('/SERVER/venv_dir'), 'bin', 'pip')
    args.yarn = 'yarn'
    return args


if Dodo.is_main(__name__, safe=True):
    args = _args()

    requirements_filename = Dodo.get_config('/SERVER/pip_requirements')

    Dodo.run([args.pip, 'install', '-r', requirements_filename])
    Dodo.run(
        [args.yarn, 'install'],
        cwd=os.path.abspath(os.path.join(args.node_modules_dir, '..')))
