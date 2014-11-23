import nose
import sys

from flask.ext.script import Command


class RunTests(Command):
    """Runs the unittests"""
    def run(self, **kwargs):
        nose.run(argv=[sys.argv[0]])
