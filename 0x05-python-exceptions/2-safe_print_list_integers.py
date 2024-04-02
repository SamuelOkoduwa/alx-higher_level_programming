#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        i = 0
        while count < x:
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end=" ")
                    count += 1
            except IndexError:
                break
            i += 1
        print()
        return count
    except Exception as error:
        print(error)

