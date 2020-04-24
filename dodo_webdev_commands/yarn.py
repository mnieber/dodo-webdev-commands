from dodo_commands import Dodo, remove_trailing_dashes


def _args():
    Dodo.parser.add_argument('yarn_args', nargs="*")
    Dodo.parser.add_argument('--name')
    args = Dodo.parse_args()
    args.yarn = 'yarn'
    args.cwd = Dodo.get_config('/WEBPACK/webpack_dir')
    return args


if Dodo.is_main(__name__, safe=True):
    args = _args()

    if args.name:
        Dodo.get_config('/DOCKER') \
            .setdefault('options', {}) \
            .setdefault('yarn', {})['name'] = args.name

    Dodo.run(
        [args.yarn] + remove_trailing_dashes(args.yarn_args), cwd=args.cwd)
