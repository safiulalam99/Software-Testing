class BankAccount:
    def __init__(self, balance=0):
        """
        Initialize a bank account with an initial balance.

        :param balance: The initial balance of the account. Default is 0.
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit an amount into the bank account.

        :param amount: The amount to be deposited.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount


    def withdraw(self, amount):
        """
        Withdraw an amount from the bank account.

        :param amount: The amount to be withdrawn.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        """
        Get the current account balance.

        :return: The current account balance.
        """
        return self.balance

    def transfer(self, target_account, amount):
        """
        Transfer money to another account.

        :param target_account: The target BankAccount object to transfer money to.
        :param amount: The amount to be transferred.
        :return: True if the transfer was successful, False otherwise.
        """
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

    def can_withdraw(self, amount):
        """
        Check if the account has enough balance for a specified transaction.

        :param amount: The amount to be checked.
        :return: True if there's enough balance, False otherwise.
        """
        return self.balance >= amount
