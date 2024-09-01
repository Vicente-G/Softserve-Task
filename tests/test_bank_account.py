from bank_account import BankAccount


def test_correct_withdraw(mocker):
    mocker.patch("builtins.input", lambda *args: "1000")
    account = BankAccount(2500)
    account.withdraw()
    assert account.balance == 1500


def test_correct_deposit(mocker):
    mocker.patch("builtins.input", lambda *args: "500")
    account = BankAccount(2500)
    account.deposit()
    assert account.balance == 3000


def test_wrong_input(mocker):
    mocker.patch("builtins.input", lambda *args: "Not a number")
    account = BankAccount(2500)
    account.withdraw()
    assert account.balance == 2500
    account.deposit()
    assert account.balance == 2500
