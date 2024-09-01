from argparse import ArgumentParser
from sys import exit

from ball_clock import clock_mode1, clock_mode2
from bank_account import BankAccount
from palindromes import palindrome_filter


def get_numbers() -> list[int]:
    try:
        return [int(word) for word in input().split()]
    except ValueError:
        return [-1, -1]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.description = "To open any of the task's questions, use the -q flag."
    parser.add_argument(
        "-q",
        "--question",
        type=int,
        required=True,
        choices=[1, 2, 3],
        help="question's number",
    )
    parser.add_argument(
        "-f", "--file", type=str, help="file path for question 1"
    )
    parser.add_argument(
        "-m",
        "--mode",
        type=int,
        choices=[1, 2],
        help="clock's mode for question 3",
    )
    args = parser.parse_args()
    if args.question == 1:
        if not args.file:
            print("Please provide a file path with the -f flag")
            exit(1)
        palindrome_filter(args.file)
    elif args.question == 2:
        account = BankAccount()
        for i in range(4):
            if i < 2:
                account.deposit()
            else:
                account.withdraw()
            account.get_balance()
    else:
        if not args.mode:
            print("Please provide the clock's mode with the -m flag")
            exit(1)
        numbers = get_numbers()
        if args.mode == 1:
            clock_mode1(numbers[0])
        else:
            clock_mode2(numbers[0], numbers[1])
