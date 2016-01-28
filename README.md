# fuzzyargparse

## About
Python argparse extension with hints on unknown arguments.

[![Build Status](https://travis-ci.org/rogalski/fuzzyargparse.svg?branch=master)](https://travis-ci.org/rogalski/fuzzyargparse)
[![Coverage Status](https://coveralls.io/repos/github/rogalski/fuzzyargparse/badge.svg?branch=master)](https://coveralls.io/github/rogalski/fuzzyargparse?branch=master)

## How to use:

    import fuzzyargparse
    parser = fuzzyargparse.FuzzyArgumentParser()
    # FuzzyArgumentParser uses same API as argparse.ArgumentParser()
    parser.parse_args()

## Sample output:

    usage: app.py [-h] [-o OPTION] [-a ANOTHER]
    app.py: error: unrecognized arguments: --optionz value --nother 123
    did you mean: --option (was: --optionz)
    did you mean: --another (was: --nother)
