import os.path as osp


def palindrome_detector(text: str) -> bool:
    """
    Checks if the string received is a palindrome
    by inverting it and checking for equality.
    """
    return text == text[::-1]


def palindrome_filter(input_file: str) -> None:
    """
    Receives a filename, filters every line checking if
    the string is a palindrome. Writes an output file with
    the filtered data.
    """
    lines = []
    with open(input_file, "r") as file:
        lines = [line.strip().lower() for line in file.readlines()]
    filtered = list(filter(palindrome_detector, lines))
    route, ext = osp.splitext(input_file)
    output_file = route + "-palindromes" + ext
    with open(output_file, "w") as file:
        file.write("\n".join(filtered))
