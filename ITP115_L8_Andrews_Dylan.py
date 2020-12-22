# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Lab 8
import random

# function flips a coin and determines it based on random number
def coin():
    num = random.randrange(0,2)
    if num == 0:
        return "heads"
    elif num == 1:
        return "tails"

# function counts number of flips it takes to get three heads in a row
def experiment():
    counter = 0
    heads = 0
    while heads < 3:
        flip = coin()
        if flip == "heads":
            counter += 1
            heads += 1
        else:
            counter += 1
            heads = 0
    return counter

# main runs the experiment 10 times
def main():
    i = 0
    sum = 0
    while i < 10:
        flips = experiment()
        sum += flips
        i += 1
    print("The average for 3 heads in a row is:", str(sum/10))


main()