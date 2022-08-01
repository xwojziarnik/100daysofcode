"""
Task3:
Write a Bank class which has methods to payment and payout.
At the initialization bank should has amount equals 0.
Don't test situation when you want to payout more than bank has.
"""


class Bank:
    def __init__(self):
        self.amount = 0

    def add_money(self, money: int) -> int:
        self.amount += money

    def payout(self, money: int) -> int:
        self.amount -= money
        return money


class TestBank:
    def test_create_bank(self):
        bank = Bank()
        assert bank.amount == 0
        assert isinstance(bank, Bank)

    def test_payment(self):
        # given
        bank = Bank()

        # when
        bank.add_money(100)

        # then
        assert bank.amount == 100

    def test_twice_payment(self):
        # given
        bank = Bank()

        # when
        bank.add_money(100)
        bank.add_money(100)

        # then
        assert bank.amount == 200

    def test_payout(self):
        # given
        bank = Bank()
        bank.add_money(100)

        # when
        money = bank.payout(100)

        # then
        assert money == 100
        assert bank.amount == 0
