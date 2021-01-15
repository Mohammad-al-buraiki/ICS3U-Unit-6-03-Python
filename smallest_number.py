# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is to find the small number

import random


def smallest_number(random_list):
    # this function calculates the smallest number

    number_of_elements = len(random_list)
    smallest = random_list[0]

    for loop_counter in range(0, number_of_elements):
        small_number = random_list[loop_counter]
        if small_number < smallest:
            smallest = small_number

    return smallest


def main():

    random_list = []
    number_of_elements = 10
    print("Here is a list of random numbers")
    print("")
    for loop_counter in range(0, number_of_elements):
        generating = random.randint(1, 100)
        print("The number is {0}.".format(generating))
        random_list.append(generating)

        small = smallest_number(random_list)

    print("")
    print("The smallest number is {0}.".format((small)))
    print("")
    print("Done!")


if __name__ == "__main__":
    main()
