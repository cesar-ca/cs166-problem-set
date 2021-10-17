#!/usr/bin/env python3

from WireworldSimulator import WireworldSimulator
from Animation import Animation

import argparse

def main(path, delay):
    initial_state = WireworldSimulator.load(path)
    wireworld = WireworldSimulator(initial_state)
    Animation(wireworld, delay).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Wireworld animation')
    parser.add_argument('world', help='File path to a wireworld')
    parser.add_argument('delay', help='Delay (ms) between each frame')
    args = parser.parse_args()
    main(args.world, args.delay)