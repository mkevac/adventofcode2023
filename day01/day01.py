#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    with open('input.txt', 'r') as f:
        sum = 0
        for l in f:
            l = l.strip()

            first_digit = -1
            last_digit = -1

            for d in l:
                if d.isdigit():
                    if first_digit == -1:
                        first_digit = d
                    last_digit = d

            number = int(first_digit)*10 + int(last_digit)
            sum += number
        print(sum)

if __name__ == '__main__':
    main()