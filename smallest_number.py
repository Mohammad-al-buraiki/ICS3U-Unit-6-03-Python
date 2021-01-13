# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is to find the small number

import random


def smallest_number(random_list, number_of_elements):

    for counter in range(0, len(random_list)):
        first = random_list[counter]
        smallest = first
        break

    for counter in range(0, len(random_list)):
        small_number = random_list[counter]
        print("The number is {0}.".format(small_number))
        if small_number < smallest:
            smallest = small_number
        else:
            pass

    return smallest


def main():

    random_list = []
    elements = 10

    for counter in range(0, elements):
        generating = random.randint(1, 100)
        random_list.append(generating)

    print("Here is a list of random numbers")
    print("")
    small = smallest_number(random_list, elements)

    print("")
    print("The smalest number is {0}.".format((small)))
    print("")
    print("Done!")


if __name__ == "__main__":
    main()
