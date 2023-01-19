import numpy
import matplotlib
import pandas
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('source', help='File choosing')
arguments = parser.parse_args()
# print(arguments)

path = arguments.source
output_path = arguments.output
