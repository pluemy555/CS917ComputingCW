"""This module should filter and sort uk phone numbers from the text file provided. """
import sys


def filter_func(number):
    if '+44' in number and len(number) is 13:
        return True
    else:
        return False


if __name__ == "__main__":
    file = sys.argv[1]
    # print(file)
    with open(file, "r") as f:
        data = f.readlines()
        uk_number = []
        for line in data:
            line = line.replace('to', '').replace('\n', '').replace(' ', '')
            phone_num = ['+' + x for x in line.split('+') if x]     # split string by # but keep # in string
            phone_num = phone_num[1:]
            uk_number.append(list(filter(filter_func, phone_num)))  # filter for uk number
        uk_number = [x for x in uk_number if x != []]               # pop empty lists
        uk_number = [x for sublist in uk_number for x in sublist]   # flatten nested lists
        uk_number = [x.replace('+44', '0') for x in uk_number]      # convert +44 to 0
        uk_number = [x[:5] + ' ' + x[5:] for x in uk_number]        # space between 5th and 6th number
        uk_number.sort()
        for i in uk_number:
            print(i)

