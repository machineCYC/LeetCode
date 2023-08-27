'''
2043. Simple Bank System

2021.10.17 Sunday 12:19
'''
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.nbr_account = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (account1 <= self.nbr_account) and (account2 <= self.nbr_account):
            if self.balance[account1-1] >= money:
                self.balance[account1-1] -= money
                self.balance[account2-1] += money
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account <= self.nbr_account:
            self.balance[account-1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= self.nbr_account:
            if self.balance[account-1] >= money:
                self.balance[account-1] -= money
                return True
        else:
            return False


if __name__ == "__main__":
    # ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
    # [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]

    # Your Bank object will be instantiated and called as such:
    obj = Bank(balance=[10, 100, 20, 50, 30])

    assert obj.withdraw(3, 10) == True
    assert obj.transfer(5, 1, 20) == True
    assert obj.deposit(5, 20) == True
    assert obj.transfer(3, 4, 15) == False
    assert obj.withdraw(10, 50) == False
