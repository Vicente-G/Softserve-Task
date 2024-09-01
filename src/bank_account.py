class BankAccount:
    """
    A class to represent a bank's account operations
    based on the user's input. It allows deposits and
    withdrawals. Also it can display the balance.
    """

    def __init__(self, balance=0) -> None:
        self.balance = balance

    def get_amount_from_console(self, mode="n") -> float:
        try:
            return float(input(f"Please enter a{mode} amount: "))
        except ValueError:
            print("Please enter a valid number")
            return 0

    def deposit(self) -> None:
        amount = self.get_amount_from_console(" deposit")
        self.balance += amount

    def withdraw(self) -> None:
        amount = self.get_amount_from_console(" withdraw")
        self.balance -= amount

    def get_balance(self) -> None:
        print(f"Current balance: {self.balance}")
