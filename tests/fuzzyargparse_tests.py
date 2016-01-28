import io
import sys
import fuzzyargparse

try:
    import unittest
    unittest.TestCase.assertIn
except AttributeError:
    import unittest2 as unittest

try:
    import unittest.mock as mock
except ImportError:
    import mock

try:
    import contextlib
    contextlib.redirect_stderr
except AttributeError:
    import contextlib2 as contextlib


class FuzzyArgparseTests(unittest.TestCase):
    def setUp(self):
        self.parser = fuzzyargparse.FuzzyArgumentParser()
        self.parser.add_argument("-o", "--option")
        mock.patch('os.linesep', return_value="\n")

    def tearDown(self):
        mock.patch.stopall()

    def test_basic(self):
        stderr = self._get_fake_stream()
        with contextlib.redirect_stderr(stderr):
            namespace = self.parser.parse_args([])
        self.assertEqual(None, namespace.option)

    def test_with_misspelled_argument(self):
        stderr = self._get_fake_stream()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as ctx:
            self.parser.parse_args(["--optionz", "value"])
        self.assertEqual(2, ctx.exception.code)
        expected = "error: unrecognized arguments: --optionz value\ndid you mean: --option (was: --optionz)"
        self.assertIn(expected, stderr.getvalue())

    def test_with_misspelled_arguments(self):
        self.parser.add_argument("-a", "--another")
        stderr = self._get_fake_stream()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as ctx:
            self.parser.parse_args(["--optionz", "value", "--nother", "123"])
        self.assertEqual(2, ctx.exception.code)
        expected = "error: unrecognized arguments: --optionz value --nother 123\ndid you mean: --option (was: --optionz)\ndid you mean: --another (was: --nother)"
        self.assertIn(expected, stderr.getvalue())

    def _get_fake_stream(self):
        return io.StringIO() if sys.version_info[0] >= 3 else io.BytesIO()


if __name__ == "__main__":
    unittest.main()
