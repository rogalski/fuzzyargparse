import os
import argparse
import itertools
from gettext import gettext as _
from fuzzywuzzy import process


class FuzzyArgumentParser(argparse.ArgumentParser):
    def parse_args(self, args=None, namespace=None):
        args, argv = self.parse_known_args(args, namespace)
        if argv:
            msg = _('unrecognized arguments: %s')
            base_msg = msg % ' '.join(argv)
            self.error(os.linesep.join(itertools.chain([base_msg], self._yield_fuzzy_hints(argv))))
        return args

    def _yield_fuzzy_hints(self, argv):
        msg = _('did you mean: %s (was: %s)')
        choices = [o for action in self._get_optional_actions() for o in action.option_strings]
        for arg in argv:
            if arg.startswith(self.prefix_chars):
                hint, _ = process.extractOne(arg, choices)
                yield msg % (hint, arg)
