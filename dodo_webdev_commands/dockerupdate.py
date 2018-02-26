# noqa
from dodo_commands.extra.standard_commands import DodoCommand
from plumbum.cmd import docker


class Command(DodoCommand):  # noqa
    help = ""
    safe = False

    docker_rm = False
    docker_options = [
        ('name', 'dockerupdate')
    ]

    def handle_imp(self, **kwargs):  # noqa
        salt_cwd = self.get_config('/DOCKER/salt/cwd', '')
        if salt_cwd:
            pillar_root = self.get_config(
                'DOCKER/salt/pillar_root', './pillar'
            )
            file_root = self.get_config(
                'DOCKER/salt/file_root', '.'
            )
            args = (
                [
                    'salt-call',
                    '--local',
                    '--file-root=%s' % file_root,
                    '--pillar-root=%s' % pillar_root,
                ]
                + self.get_config('DOCKER/salt/extra_args', [])
                + [
                    'state.apply'
                ]
            )
            self.runcmd(args, cwd=salt_cwd)
        else:
            return

        container_id = docker("ps", "-l", "-q")[:-1]
        docker("commit", container_id, self.get_config("/DOCKER/image"))
        docker("rm", container_id)
