#!/usr/bin/python

import os
import sys
import subprocess
import unittest

sys.path.insert(0, os.path.abspath('..'))
from realpath import realpath


class RealpathTest(unittest.TestCase):

    def test_basic(self):
        examples = [
            '.',
            '..',
            'foo',
            'foo/bar',
            '/bar',
            '/bar/baz',
        ]

        pwd = os.popen('pwd').read().strip()
        for ex in examples:
            expected = os.path.abspath(os.path.join(pwd, ex))
            res = realpath(ex)
            self.assertEqual(expected, res)



if __name__ == '__main__':
    unittest.main()
