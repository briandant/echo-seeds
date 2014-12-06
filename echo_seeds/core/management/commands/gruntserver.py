import os
import subprocess
import atexit
import signal

from django.conf import settings
from django.contrib.staticfiles.management.commands.runserver import Command\
    as StaticFilesRunserverCommand


class Command(StaticFilesRunserverCommand):

    def inner_run(self, *args, **options):
        self.start_grunt()
        return super(Command, self).inner_run(*args, **options)

    def start_grunt(self):
        self.stdout.write(">>> Starting Grunt")
        self.grunt_process = subprocess.Popen(
            ['grunt dev --gruntfile={0}/Gruntfile.js --base=.'.format(settings.PROJECT_DIR)],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=self.stdout,
            stderr=self.stderr
        )

        self.stdout.write(
            '>>> Grunt Process Running pid {0}'.format(self.grunt_process.pid)
        )

        def kill_grunt_process(pid):
            self.stdout.write(">>> Closing Grunt process")
            os.kill(pid, signal.SIGTERM)

        atexit.register(kill_grunt_process, self.grunt_process.pid)
