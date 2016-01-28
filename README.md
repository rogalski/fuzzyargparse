# fuzzyargparse

## About
Python argparse extension with hints on unknown arguments.

[![Build Status](https://travis-ci.org/rogalski/fuzzyargparse.svg?branch=master)](https://travis-ci.org/rogalski/fuzzyargparse)
[![Coverage Status](https://coveralls.io/repos/github/rogalski/fuzzyargparse/badge.svg?branch=master)](https://coveralls.io/github/rogalski/fuzzyargparse?branch=master)
[![Code Climate](https://codeclimate.com/github/rogalski/fuzzyargparse/badges/gpa.svg)](https://codeclimate.com/github/rogalski/fuzzyargparse)

## License
[The MIT License](LICENSE).

## Dependencies

Fuzzyargparse uses:
- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) is used for fuzzy string matching
- [python-Levenshtein](https://pypi.python.org/pypi/python-Levenshtein) should be installed for performance increase

## How to use:

    import fuzzyargparse
    parser = fuzzyargparse.FuzzyArgumentParser()
    parser.add_argument("-o", "--option")
    parser.add_argument("-a", "--another")
    parser.parse_args()

## Sample output:

    usage: app.py [-h] [-o OPTION] [-a ANOTHER]
    app.py: error: unrecognized arguments: --optionz value --nother 123
    did you mean: --option (was: --optionz)
    did you mean: --another (was: --nother)
