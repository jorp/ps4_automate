#!/usr/bin/env python3
import os
import re
import sys

with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        match = re.match(r"([0-9]+)([a-z]+)", line, re.I)
        if match:
            items = match.groups()
        print(items)
