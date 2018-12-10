#!/usr/bin/env python3

import os

def print_renaming_list(ls):
    if len(ls) == 0:
        print ('Nothing to be done')
        exit()
    print ('Will rename {} {}'.format(
        len(ls), 'file' if len(ls) == 1 else 'files'))
    for fileFrom, fileTo in ls:
        print ('* {}\t-->\t{}'.format(fileFrom, fileTo))


def confirm():
    """
    Ask user to enter Y or N (case-insensitive).
    :return: True if the answer is Y.
    :rtype: bool
    """
    answer = ""
    while answer not in ["y", "n"]:
        answer = input("OK to push to continue [Y/N]? ").lower()
        return answer == "y"

def main():
    target_string = ' 的副本'
    files = [f for f in os.listdir()
            if os.path.isfile(f)
            and f.endswith(target_string)]
    renaming_list = [(f, f[:-len(target_string)]) for f in files]
    print_renaming_list(renaming_list)

    if not confirm():
        print ('Cancelled')
    else:
        for fileFrom, fileTo in renaming_list:
            os.rename(fileFrom, fileTo)
        print ('Complete')

if __name__ == '__main__':
    main()

