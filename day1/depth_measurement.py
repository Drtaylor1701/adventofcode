#! /usr/bin/env python3

def count_increases():
    with open("day1/input.txt") as depths:
        oldline = depths.readline()
        increases = 0
        for line in depths:
            if line <= oldline:
                continue
            else:
                increases += 1
            oldline = line
    return increases

count_increases()