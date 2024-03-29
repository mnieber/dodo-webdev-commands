# Version history

## 0.20.0

- Update command signatures
- Add new commands and remove install-packages
- Fix: make_args in make.py
- Remove --cov from pytest

## 0.19.0

- Fix: Use /NODE/cwd in dodo yarn
- Fix: Use dodo_commands.dependencies.get
- Fix: Use /DOCKER_IMAGES

## 0.18.0

- Remove obsolete commands, prefer Makefiles
- Add node, nps and make
- Use cwd instead of src_dir in config

## 0.17.0

- Allow /PYTEST/pytest to be an array

## 0.16.0

- Add flow-install-types
- Read pytest exe from /PYTEST/pytest
- Add yapf commands
- Add unused-imports.py
- Add flow.py
- Add option --manage-py to django-runserver
- Add flag --reuse-db to dodo pytest
- Support setting node_modules_dir to default in install-packages

## 0.15.1

- Remove obsolete command dodo psql
- Rename command to download-dump
- Use argument pg_version in run-postgres
- Use --pip-requirements argument in install-packages

## 0.15.0

- Add jekyll-bundle command
- Remove use of Dodo.config

## 0.14.0

Add --name argument to yarn
Refactor install-packages
Add commands: psql, yarn, rtop download_dump, prod-to-staging, run-memcached
Fix tape command
Rename runcmd to run, and apply yapf

## 0.13.3

- Format all python files with yapf

## 0.13.2

- Fix commands broken by refactoring

## 0.13.1

- Add docker_update helper module

## 0.13.0

- Synchronize major version number with dodo commands
- Remove dockerupdate command
- Move dockercreate and dockerexec to standard commands
- Remove docker_options attribute
- Add script_args argument to dodo python

## 0.7.1

- Fix: import input command from six.moves

## 0.7.0

- Make dockerupdate a generic command
- Add dockercreate command
- Don't kill docker containers in dodo tmux

## 0.6.0

- Use value /DJANGO/port in django-runserver
- Allow to omit the name argument in dockerexec
- Use values /PYTEST/capture, html_report test_file in pytest
- Use value /TMUX/check_exists in dodo tmux

## 0.5.2

- Add option --only-kill to tmux command

## 0.5.1

- Fix ansible call in dockerupdate when no tags are supplied

## 0.5.0

- Update to the new /DOCKER/options format

## 0.4.0

- Remove list of decorators from the DodoCommand class

## 0.3.0

- Add commands: ansible-playbook, dockerupdate, runpostgres, runserver
- Use remove_trailing_dashes in dodo autoless

## 0.2.0

- Allow multiple inputs and outputs in node-sass by using /SASS/src_map

## 0.1.0

- Initial version
