import brackets as b

bb = b.Brackets()
print("utest_balance.py is in module: ", __name__)
def utest_balance():
    """
    unit test to check:
    edge cases '' ' ' '('
    cheat sheet 0 0 1
    """
    assert bb.balance_brackets('') == 0
    assert bb.balance_brackets(' ') == 0
    assert bb.balance_brackets('(') == 1
    assert bb.balance_brackets('())') == 1
    assert bb.balance_brackets('())(') == 2
