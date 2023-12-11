#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fix_line(l):

    digits = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9,
    }

    # not good, see example:
    # pxreightwo7
    # pxreigh27
    # 
    # for ds, dv in digits.items():
    #     l = l.replace(ds, str(dv))

    lowestindex = 1
    lowestnumber = 1

    while lowestindex != -1:

        lowestindex = -1
        lowestnumber = -1

        for (ds, dv) in digits.items():
            i = l.find(ds)
            if i != -1:
                if lowestindex == -1 or i < lowestindex:
                    lowestindex = i
                    lowestnumber = ds

        if lowestindex != -1:
            to_put = lowestnumber[0] + str(digits[lowestnumber]) + lowestnumber[-1]
            l = l[:lowestindex] + to_put + l[lowestindex+len(lowestnumber):]
    return l

def get_calibration_number(l):
    first_digit = -1
    last_digit = -1

    for d in l:
        if d.isdigit():
            if first_digit == -1:
                first_digit = d
            last_digit = d

    number = int(first_digit)*10 + int(last_digit)
    return number

def main():
    with open('input.txt', 'r') as f:
        sum = 0
        for l in f:
            l = l.strip()
            print("was", l)
            l = fix_line(l)
            print("now", l)

            number = get_calibration_number(l)
            print("number", number)

            sum += number
            print("sum", sum)

        print(sum)

if __name__ == '__main__':
    main()