import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("range", type=int, help='an integer to pass to numpy')
args = parser.parse_args()

range = args.range
size = range * 2

a = np.arange(size).reshape(range, 2)

print(a)