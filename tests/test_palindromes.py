from typing import Callable

from palindromes import palindrome_filter

EXAMPLE = """rotor
Dad
kayaks
Sad
kayak"""
ANSWER = """rotor
dad
kayak"""

output = ""


class BufferMock:
    def __init__(self, data, return_filename) -> None:
        self.content = data
        self.return_filename = return_filename

    def readlines(self) -> list[str]:
        return self.content.split("\n")

    def write(self, text) -> None:
        global output
        output = self.content if self.return_filename else text

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


def open_mock(return_filename=False) -> Callable[[str, str], BufferMock]:
    def fake_open(filename, mode) -> BufferMock:
        if mode == "r":
            return BufferMock(EXAMPLE, return_filename)
        return BufferMock(filename, return_filename)

    return fake_open


def test_correct_example(mocker):
    mocker.patch("builtins.open", open_mock())
    palindrome_filter("input.txt")
    assert output == ANSWER


def test_correct_output_filename(mocker):
    mocker.patch("builtins.open", open_mock(return_filename=True))
    palindrome_filter("input.txt")
    assert output == "input-palindromes.txt"
