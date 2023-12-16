#!/usr/bin/env python3
# -*- coding: utf-8 -*-

contains = {'red': 12, 'green': 13, 'blue': 14}

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

def check_handful(handful):
    if handful.get('red', 0) > contains['red']:
        return False
    if handful.get('green', 0) > contains['green']:
        return False
    if handful.get('blue', 0) > contains['blue']:
        return False
    return True

def main():
    print("Contains {}" % contains)
    sum = 0
    with open('input.txt', 'r') as f:
        for l in f:
            l = l.strip()
            game = parse_line(l)
            game_possible = True
            for handful in game['handfuls']:
                if check_handful(handful) == True:
                    print('[✅] Game %s: Handful: %s' % (game['game'], handful))
                    continue
                else:
                    print('[❎] Game %s: Handful: %s' % (game['game'], handful))
                    game_possible = False
                    break
            if game_possible == True:
                sum += game['game']
    print(sum)

if __name__ == '__main__':
    main()