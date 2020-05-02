from dodo_commands import Dodo


def _args():
    Dodo.parser.add_argument('pytest_args', nargs="*")
    args = Dodo.parse_args()
    args.no_capture = not Dodo.get_config("/PYTEST/capture", True)
    args.reuse_db = Dodo.get_config("/PYTEST/reuse_db", False)
    args.html_report = Dodo.get_config("/PYTEST/html_report", None)
    args.test_file = Dodo.get_config("/PYTEST/test_file", None)
    args.pytest_ini_filename = Dodo.get_config("/PYTEST/pytest_ini", None)
    args.maxfail = Dodo.get_config("/PYTEST/maxfail", None)
    args.pytest = Dodo.get_config("/PYTEST/pytest", "pytest")
    args.cwd = Dodo.get_config("/PYTEST/cwd", Dodo.get_config("/ROOT/src_dir"))
    return args


if Dodo.is_main(__name__):
    args = _args()

    run_args = [
        *(args.pytest if isinstance(args.pytest, list) else [args.pytest]),
        *([args.test_file] if args.test_file else []),
        *(["--capture", "no"] if args.no_capture else []),
        *(["--reuse-db"] if args.reuse_db else []),
        *(["-c", args.pytest_ini_filename]
          if args.pytest_ini_filename else []),
        *(["--maxfail", str(args.maxfail)] if args.maxfail else []),
        *(["--html", args.html_report] if args.html_report else []),
    ]

    Dodo.run(run_args, cwd=args.cwd)
