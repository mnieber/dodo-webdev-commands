from argparse import ArgumentParser
from dodo_commands.framework import Dodo, CommandError
import os


def _args():
    parser = ArgumentParser()
    args = Dodo.parse_args(parser)
    return args


if Dodo.is_main(__name__):
    args = _args()
    check_exists = Dodo.get_config('/TMUX/check_exists', '/')
    if not os.path.exists(check_exists):
        raise CommandError("Path %s does not exist" % check_exists)

    default_script = os.path.join(
        Dodo.get_config("/ROOT/res_dir"),
        "tmux.sh"
    )
    tmux_script = Dodo.get_config("/TMUX/script_file", default_script)
    Dodo.runcmd(["chmod", "+x", tmux_script])
    Dodo.runcmd([tmux_script])
