def poker(hands):
    "Return the best hand: poker([hand1, hand2, ....]) ==> hand1"
    return max(hands, key=hand_rank)


def straight(hand):
    pass


def flush(hand):
    pass


def card_ranks(hand):
    "Convert cards into numbers"
    return 0

def kind(num,hand):
    "return maximum number of card occur"

    pass


def hand_rank(hand):
    "Return a value indicating the ranking of a hand"

    ranks = card_ranks(hand)

    if straight(ranks) and flush(hand):
        return (8,max(ranks))
    elif kind(4, ranks):
        return (7, kind(4,ranks), kind(1,ranks))





def test():
    "Test cases for the functions in poker program"

    # Straight flush
    sf = "6C 7C 8C 9C TC".split()
    
    # full
    fk = "9D 9H 9S 9C 7D".split()

    # Full House
    fh = "TD TC TH 7C 7D".split()

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