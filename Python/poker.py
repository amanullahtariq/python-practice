import random

hand_names = ['High Card', 'Pair', '2 Pair', '3 of a Kind', 'Straight', 'Flush', 'Full House', '4 of a Kind',
              'Straight Flush']


def poker(hands):
    """
    Return a list of winning hands: poker([hand,.....]) = > [hand,....]
    """
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    """
    Return a list of all items equal to the max of the iterable.
    :param iterable:
    :param key:
    :return:
    """

    result = []
    maxval = None

    key = key or (lambda x: x)

    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)

    return result


def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5)


def is_flush(hand):
    "Return True if all the cards have the same suit"

    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    """
    Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand.
    """
    for r in ranks:
        if ranks.count(r) == n: return r

    return None


def two_pair(ranks):
    """
    if there are two pair, return two ranks as a
    tuple: (highest, lowest); other return None.
    """
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))

    if pair and low_pair != pair:
        return (pair, low_pair)

    return None


def card_ranks(cards):
    """
    Returns an ORDERED tuple of the ranks in a hand
    (where the order goes from highest to lowest
    rank).

    :param hand:
    :return:
    """
    hand_list = '--23456789TJQKA'
    ranks = [hand_list.index(r) for r, s in cards]
    ranks.sort(reverse=True)

    return [5, 4, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def group(items):
    """
    Retunrs a lis of [(count,x) ...] , highest count first, then highest x first.
    :param items:
    :return:
    """
    groups = [(items. count(x),x) for x in set(items)]

    # highest come first
    return sorted(groups, reverse=True)


def unzip(pairs):
    return zip(*pairs)


def hand_rank(hand):
    """
    Return a value indicating how high the hand ranks

    """

    # counts is the count of each rank; ranks lists corresponding ranks
    # E.g. '7 T 7 9 7' => counts = (3,1,1) ; ranks = (7,10,9)]

    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = unzip(groups)

    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)

    straight = len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4
    flush = is_flush(hand)

    return max(count_rankings[counts], 4* straight + 5*flush), ranks

count_rankings = {(5,) : 10 , (4,1): 7, (3,2): 6, (3,1,1):3, (2,2,1):2, (2,1,1,1):1, (1,1,1,1,1):0}


#
# def test():
#     """
#     Test cases for the functions in poker program
#     :return:
#     """
#
#     # Straight flush
#     sf = "6C 7C 8C 9C TC".split()
#
#     # four of a kind
#     fk = "9D 9H 9S 9C 7D".split()
#
#     # Full House
#     fh = "TD TC TH 7C 7D".split()
#
#     # two pair
#     tp = "5S 5D 9H 9C 6S".split()
#
#     # A-5 straight
#     s1 = "AS 2S 3S 4S 5C".split()
#
#     # 2-6 straight
#     s2 = "2C 3C 4C 5S 6S"
#
#     # A High
#
#     # 7-High
#     sh = "2S 3S 4S 6C 7D".split()
#
#     fkranks = card_ranks(fk)
#     tpranks = card_ranks(tp)
#
#     assert kind(4, fkranks) == 9
#     assert kind(3, fkranks) == None
#     assert kind(2, fkranks) == None
#     assert kind(1, fkranks) == 7
#
#     assert two_pair(fkranks) == None
#     assert two_pair(tpranks) == (9, 5)
#
#     assert straight([9, 8, 7, 6, 5]) == True
#     assert straight([9, 8, 8, 6, 5]) == False
#
#     assert flush(sf) == True
#     assert flush(fk) == False
#
#     assert card_ranks(sf) == [10, 9, 8, 7, 6]
#     assert card_ranks(fk) == [9, 9, 9, 9, 7]
#     assert card_ranks(fh) == [10, 10, 10, 7, 7]
#
#     # assert poker([sf, fk, fh]) == fh
#     # assert poker([fk, fh]) == fk
#     # assert poker([fh,fh]) == fh
#     # assert poker([sf]) == sf
#     # assert poker([sf] + 99*[fh]) == sf
#
#     assert hand_rank(sf) == (8, 10)
#     assert hand_rank(fk) == (7, 9, 7)
#     assert hand_rank(fh) == (6, 10, 7)
#
#     return 'tests pass'


mydeck = [r + s for r in '2345679TJQKA' for s in 'SHDC']


def deal(numhands, n=5, deck=mydeck):
    """
    take a deck shuffle it and
    :param numhands: number of players
    :param n: number of cards
    :param deck: deck of cards to use
    :return:
    """

    random.shuffle(deck)

    return [deck[n * i: n * (i + 1)] for i in range(numhands)]


def hand_percentage(n=700 * 1000):
    """
    Sample n random hands and print a table of percentages for each type of hand
    :param n:
    :return:
    """
    counts = [0] * 9

    for i in range(int(n / 10)):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1

    for i in reversed(range(9)):
        print("%14s: %6.3f %%" % (hand_names[i], 100.0 * counts[i] / n))


print( deal(2,7))
