import io
import contextlib
import fuzzyargparse

try:
    import unittest
except ImportError:
    import unittest2 as unittest

try:
    import unittest.mock as mock
except ImportError:
    import mock


class FuzzyArgparseTests(unittest.TestCase):
    def setUp(self):
        self.parser = fuzzyargparse.FuzzyArgumentParser()
        self.parser.add_argument("-o", "--option")
        mock.patch('os.linesep', return_value="\n")

    def tearDown(self):
        mock.patch.stopall()

    def test_basic(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            namespace = self.parser.parse_args([])
        self.assertEqual(None, namespace.option)

    def test_with_misspelled_argument(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as ctx:
            self.parser.parse_args(["--optionz", "value"])
        self.assertEqual(2, ctx.exception.code)
        expected = "error: unrecognized arguments: --optionz value\ndid you mean: --option (was: --optionz)"
        self.assertIn(expected, stderr.getvalue())

    def test_with_misspelled_arguments(self):
        self.parser.add_argument("-a", "--another")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as ctx:
            self.parser.parse_args(["--optionz", "value", "--nother", "123"])
        self.assertEqual(2, ctx.exception.code)
        expected = "error: unrecognized arguments: --optionz value --nother 123\ndid you mean: --option (was: --optionz)\ndid you mean: --another (was: --nother)"
        self.assertIn(expected, stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
