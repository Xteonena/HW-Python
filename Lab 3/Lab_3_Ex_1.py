class BankAccount:
    """
    A class representing a bank account.
    """
    def __init__(self, account_number: int, name: str, balance: float, password: str):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount: float) -> str:
        """
        Adds the specified amount to the bank account balance.

        Args:
            amount (float): The amount to be added to the bank account balance.

        Returns:
            str: A string indicating that the amount has been successfully credited to the account.
        """
        self.balance += amount
        return "Amount {} has been successfully credited to your account".format(amount)

    def withdrawal(self, amount: float) -> str:
        """
        Subtracts the specified amount from the bank account balance, if the account has sufficient funds.

        Args:
            amount (float): The amount to be subtracted from the bank account balance.

        Returns:
            str: A string indicating that the amount has been successfully withdrawn from the account,
                or a string indicating that there are insufficient funds on the account.
        """
        if self.balance >= amount:
            self.balance -= amount
            return "Amount {} has been successfully withdrawn from the account".format(amount)
        else:
            return "Insufficient funds on the account"

    def bank_fees(self) -> None:
        """
        Applies a bank fee to the bank account balance.
        """
        self.balance *= 0.95

    def display(self) -> str:
        """
        Returns a string containing the account number, name, and balance.

        Returns:
            str: A string containing the account number, name, and balance.
        """
        return "Account number: {}\nName: {}\nBalance: {}".format(self.account_number, self.name, self.balance)

    # Added an extra method to make it more fun
    def authorize(self, account_number: int, password: str) -> bool:
        """
        Returns True if the specified account number and password match the account number
        and password associated with the bank account, otherwise returns False.

        Args:
            account_number (int): The account number to be checked.
            password (str): The password to be checked.

        Returns:
            bool: True if the account number and password match, otherwise False.
        """
        if account_number == self.account_number and password == self.password:
            return True
        else:
            return False


# Creating an object of class BankAccount
account = BankAccount(0, "Krupin Dmitriy", 200000, "12345")
account1 = BankAccount(1, "Cai Maksim", 250000, "54321")

# User authorization
while not account.authorize(int(input("Enter account number: ")), input("Enter password: ")):
    print("Invalid account number or password")

# Checking the methods of the BankAccount class
account.deposit(int(input("Enter the replenishment amount: ")))  # Adding to account balance
account.withdrawal(int(input("Enter the amount to withdraw: ")))  # Withdrawal of funds from the account
account.bank_fees()  # Application of bank fees
print(account.display())  # Displaying account information
