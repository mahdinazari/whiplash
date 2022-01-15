import argparse

from .benchmark import Benchmark


parser = argparser.ArgumentParser()
parser.add_argument(
    'command',
    choices=['benchmark'],
    help='You can choose the benchmark command to start'
)
parser.add_argument(
    'number of requests',
    type=int,
    help='Number of requests'
)
parser.add_arguments=(
    '-c',
    'concurrency',
    type=int,
    nargs='+'
    help='Number of concurrency requests'
)


