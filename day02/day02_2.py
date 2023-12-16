#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example line to parse: Game 1: 1 red, 5 blue, 1 green; 16 blue, 3 red; 6 blue, 5 red; 4 red, 7 blue, 1 green
"""
def parse_line(l):
    game = l.split(':')[0].split(' ')[1]
    handfuls = []
    for h in l.split(':')[1].split(';'):
        handful = {}
        for c in h.split(','):
            n, color = c.strip().split(' ')[0], c.strip().split(' ')[1]
            handful[color] = int(n)
        handfuls.append(handful)
    return {'game': int(game), 'handfuls': handfuls}

def get_power(handfuls):
    max_red = 0
    max_green = 0
    max_blue = 0

    for handful in handfuls:
        if handful.get('red', 0) > max_red:
            max_red = handful.get('red', 0)
        if handful.get('green', 0) > max_green:
            max_green = handful.get('green', 0)
        if handful.get('blue', 0) > max_blue:
            max_blue = handful.get('blue', 0)

    return max_red*max_green*max_blue

def main():
    sum = 0
    with open('input.txt', 'r') as f:
        for l in f:
            l = l.strip()
            game = parse_line(l)
            sum += get_power(game['handfuls'])
    print(sum)

if __name__ == '__main__':
    main()