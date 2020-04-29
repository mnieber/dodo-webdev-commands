from dodo_commands import Dodo


def _args():
    Dodo.parser.add_argument('yarn_args', nargs="*")
    Dodo.parser.add_argument('--name')
    args = Dodo.parse_args()
    args.yarn = 'yarn'
    args.cwd = Dodo.get_config('/NODE/cwd')
    return args


if Dodo.is_main(__name__, safe=True):
    args = _args()

    if args.name:
        Dodo.get_config('/DOCKER') \
            .setdefault('options', {}) \
            .setdefault('yarn', {})['name'] = args.name

    Dodo.run(
        [args.yarn, *args.yarn_args], cwd=args.cwd)
