import itertools
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


def best_hand(hand):
    """
    From a 7-card hand, return the best 5 card hand.
    :param hand:
    :return:
    """

    return  max(itertools.combinations(hand,5),key=hand_rank)




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


def best_wild_hand(hand):
    """
    Try all values for jokers in all 5-card selections

    :param hand:
    :return:
    """

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'