#!/usr/bin/python

#!/usr/bin/python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

input = open(from_file, to_file, 'r')

input.write(to_file)

input.close()

