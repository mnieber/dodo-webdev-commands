from dodo_commands import Dodo


def _args():
    Dodo.parser.add_argument("script")
    Dodo.parser.add_argument("script_args", nargs="*")
    args = Dodo.parse_args()
    args.python = Dodo.get_config("/PYTHON/python")
    args.cwd = Dodo.get_config("/PYTHON/cwd")
    return args


if Dodo.is_main(__name__):
    args = _args()
    Dodo.run([args.python, args.script, *args.script_args], cwd=args.cwd)
