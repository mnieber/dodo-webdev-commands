# noqa
from dodo_commands.extra.standard_commands import DodoCommand, CommandError
from plumbum.cmd import docker


class Command(DodoCommand):  # noqa
    help = ""

    def add_arguments_imp(self, parser):  # noqa
        parser.add_argument('--playbook')
        parser.add_argument('--input-image')

    def _playbook(self, playbook):
        return playbook or self.get_config("/ANSIBLE/default_playbook")

    def _input_image_name(self, input_image):
        return input_image or self.get_config("/DOCKER/image")

    @property
    def _output_image_name(self):
        return self.get_config("/DOCKER/image")

    @property
    def _ansible_dir(self):
        return self.get_config("/ANSIBLE/src_dir")

    @property
    def _remote_ansible_dir(self):
        return "/root/ansible/"

    def _check_existing_image(self, input_image):
        input_image_name = self._input_image_name(input_image)
        result = docker("images", "-a", "--quiet", input_image_name)
        if not result:
            raise CommandError("Cannot find image %s" % input_image_name)

    def handle_imp(self, playbook, input_image, **kwargs):  # noqa
        self._check_existing_image(input_image)
        self.runcmd(
            [
                "docker",
                "run",
                "-w", self._remote_ansible_dir,
                "--volume=%s:%s" % (self._ansible_dir, self._remote_ansible_dir),
                self._input_image_name(input_image),
                "/bin/bash",
                "-c",
                "ansible-playbook -i hosts -l localhost %s" % self._playbook(playbook)
            ]
        )

        container_id = docker("ps", "-l", "-q")[:-1]
        self.runcmd(["docker", "commit", container_id, self._output_image_name])
        self.runcmd(["docker", "rm", container_id])
