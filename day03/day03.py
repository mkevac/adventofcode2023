#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def adjacent_stars(db, line, start, end):
    stars = []

    # look left
    if start > 0:
        if db[line][start-1] == '*':
            stars.append((line, start-1))

    # look right
    if end < len(db[line])-1:
        if db[line][end+1] == '*':
            stars.append((line, end+1))

    # look on previous line
    if line > 0:
        line_to_check = line-1
        start_to_check = start-1 if start > 0 else start
        end_to_check = end+1 if end < len(db[line])-1 else end

        for x in range(start_to_check, end_to_check+1):
            if db[line_to_check][x] == '*':
                stars.append((line_to_check, x))

    # look on next line
    if line < len(db)-1:
        line_to_check = line+1
        start_to_check = start-1 if start > 0 else start
        end_to_check = end+1 if end < len(db[line])-1 else end

        for x in range(start_to_check, end_to_check+1):
            if db[line_to_check][x] == '*':
                stars.append((line_to_check, x))

    return stars

def check_adjacent(db, line, start, end):
    # look left
    if start > 0:
        if db[line][start-1] != '.':
            return True

    # look right
    if end < len(db[line])-1:
        if db[line][end+1] != '.':
            return True

    # look on previous line
    if line > 0:
        line_to_check = line-1
        start_to_check = start-1 if start > 0 else start
        end_to_check = end+1 if end < len(db[line])-1 else end

        for x in range(start_to_check, end_to_check+1):
            if db[line_to_check][x] != '.':
                return True

    # look on next line
    if line < len(db)-1:
        line_to_check = line+1
        start_to_check = start-1 if start > 0 else start
        end_to_check = end+1 if end < len(db[line])-1 else end

        for x in range(start_to_check, end_to_check+1):
            if db[line_to_check][x] != '.':
                return True

    return False

def main():
    sum = 0
    db = []
    with open('input.txt', 'r') as f:
        for l in f:
            db.append(l.strip())

    for (line_no, line) in enumerate(db):
        matches = re.finditer(r'(\d+)', line)
        for match in matches:
            if check_adjacent(db, line_no, match.start(), match.end()-1):
                sum += int(match.group())
    
    print(sum)

    # part 2

    stars = {}

    for (line_no, line) in enumerate(db):
        matches = re.finditer(r'(\d+)', line)
        for match in matches:
            adst = adjacent_stars(db, line_no, match.start(), match.end()-1)
            for s in adst:
                n = stars.get(s, [])
                n.append(int(match.group()))
                stars[s] = n
    
    sum = 0
    for (k, v) in stars.items():
        if len(v) > 1:
            sum = sum + (v[0] * v[1])

    print(sum)
if __name__ == '__main__':
    main()