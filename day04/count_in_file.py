import sys


def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} <filename>")

    filename = sys.argv[1]

    with open(filename, "r") as fh:
        text = fh.read()
        words_in_text = text.split()
        print(f"The number of words in the file is {len(words_in_text)}")

        # Calculate the number of lines by counting newline characters
        number_of_lines = text.splitlines()
        print(f"The number of lines in the file is {len(number_of_lines)}")

        # Calculate the number of unique characters
        char_set = set(text)
        print(f"The number of unique characters in the file is {len(char_set)}")

        # Calculate the total number of characters
        total_chars = len(text)
        print(f"The number of characters in the file is {total_chars}")


main()
