import greet
import sys

names = sys.argv[1:]
for name in names:
    print(greet.greet(name))
