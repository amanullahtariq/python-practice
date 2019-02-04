def poker(hands):
    "Return the best hand: poker([hand1, hand2, ....]) ==> hand1"
    return max(hands, key=hand_rank)


def straight(ranks):
     "Return True if the ordered ranks form a 5-card straight."
     return  (max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5)



def flush(hand):
    "Return True if all the cards have the same suit"

    suits = [s for r,s in hand]
    return len(set(suits)) == 1



def kind(n,ranks):
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
        return (pair,low_pair)

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
    ranks = [ hand_list.index(r) for r, s in cards]
    ranks.sort(reverse=True)

    return [5,4,2,1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def hand_rank(hand):
    """
    Return a value indicating the ranking of a hand
    """

    #Get the card in the sorted order
    ranks = card_ranks(hand)

    # straight flush
    if straight(ranks) and flush(hand):
        return (8,max(ranks))

    # 4 of a kind
    elif kind(4, ranks):
        return (7, kind(4,ranks), kind(1,ranks))

    # full house
    elif kind(3, ranks) and kind(2,ranks):
        return(6,kind(3,ranks), kind(2,ranks))

    # flush
    elif flush(hand):
        return(5, ranks)

    # Straight
    elif straight(ranks):
        return (4, max(ranks))

    # 3 of a kind
    elif kind(3,ranks):
        return (3, kind(3,ranks) , ranks)

    # Two-pair
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)

    # Kind
    elif kind(2, ranks):
        return (1, kind(2, ranks) , ranks)

    # Nothing
    else:
        return (0, ranks)


def test():
    """
    Test cases for the functions in poker program
    :return:
    """

    # Straight flush
    sf = "6C 7C 8C 9C TC".split()
    
    # four of a kind
    fk = "9D 9H 9S 9C 7D".split()

    # Full House
    fh = "TD TC TH 7C 7D".split()

    # two pair
    tp = "5S 5D 9H 9C 6S".split()

    # A-5 straight
    s1 = "AS 2S 3S 4S 5C".split()

    # 2-6 straight
    s2 = "2C 3C 4C 5S 6S"

    # A High



    # 7-High
    sh = "2S 3S 4S 6C 7D".split()

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert  kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2,fkranks) == None
    assert kind(1,fkranks) == 7

    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9,5)

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh,fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf

    assert hand_rank(sf) == (8,10)
    assert hand_rank(fk) == (7,9,7)
    assert hand_rank(fh) == (6,10,7)


    return 'tests pass'


test()