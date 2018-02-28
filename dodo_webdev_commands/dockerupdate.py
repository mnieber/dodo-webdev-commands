# noqa
from dodo_commands.extra.standard_commands import DodoCommand
from dodo_commands.framework.config_expander import Key
from plumbum.cmd import docker


class Command(DodoCommand):  # noqa
    help = ""
    safe = False

    docker_rm = False
    docker_options = [
        ('name', 'dockerupdate')
    ]

    def add_arguments_imp(self, parser):  # noqa
        parser.add_argument('name')

    def handle_imp(self, name, **kwargs):  # noqa
        docker_image = self.get_config('DOCKER/images/%s/image' % name, name)

        xpath = 'DOCKER/options/dockerupdate/image'.split('/')
        Key(self.config, xpath).set(docker_image)

        salt_config = self.get_config('DOCKER/images/%s/salt' % name, {})
        if salt_config:
            args = (
                [
                    'salt-call',
                    '--local',
                    '--file-root=%s' % salt_config.get('file_root', '.'),
                    '--pillar-root=%s' % salt_config.get(
                        'pillar_root', './pillar'
                    ),
                ]
                + self.get_config('DOCKER/salt/extra_args', [])
                + [
                    'state.apply'
                ]
            )
            self.runcmd(args, cwd=salt_config['cwd'])
        else:
            return

        container_id = docker("ps", "-l", "-q")[:-1]
        docker("commit", container_id, docker_image)
        docker("rm", container_id)
