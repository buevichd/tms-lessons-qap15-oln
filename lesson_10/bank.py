import random


def get_random_digits(count: int) -> str:
    result = ''
    for _ in range(count):
        result += str(random.randint(0, 9))
    return result


class BankAccount:
    def __init__(self, card_holder):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = get_random_digits(20)
        self.card_number = get_random_digits(16)


class Bank:
    def __init__(self):
        self.bank_accounts: dict[str, BankAccount] = {}

    def open_account(self, card_holder) -> BankAccount:
        account = BankAccount(card_holder)
        self.bank_accounts[account.account_number] = account
        return account

    def add_money(self, account_number: str, money: float):
        target_account = self.bank_accounts[account_number]
        target_account.money += money

