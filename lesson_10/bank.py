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

    def transfer_money(self, from_account_number,
                       to_account_number, money):
        from_account = self.bank_accounts[from_account_number]
        to_account = self.bank_accounts[to_account_number]
        from_account.money -= money
        to_account.money += money

    def external_transfer(self, from_account_number,
                          to_external_number, money):
        from_account = self.bank_accounts[from_account_number]
        from_account.money -= money

        print(f'Банк перевёл {money}$ с вашего счёта '
              f'{from_account_number} на внешний счёт '
              f'{to_external_number}')


class Controller:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        print('Здравствуйте, наш банк открылся!')


if __name__ == '__main__':
    controller = Controller()
    controller.run()

