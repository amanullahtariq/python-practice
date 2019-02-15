# The Fisher shuffle aglorithm

import random


def shuffle(deck):
    """
    Knuth's Algorithm P.

    :param deck:
    :return:
    """
    N = len(deck)

    for i in range(N -1):
        swap(deck, i , random.randrange(i,N))

    return  deck
def swap(deck, i , j):
    """
    Swap elelments i and j of a collection

    :param deck:
    :param i:
    :param j:
    :return:
    """
    # print('swap ', i , j)
    deck[i], deck[j] = deck[j], deck[i]



input = list('abcd')
print(shuffle(input))

input = list('abc')
print(shuffle(input))


