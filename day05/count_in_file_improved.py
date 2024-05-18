import sys
import counter

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} <filename>")

    filename = sys.argv[1]
    with open(filename, "r") as fh:
        text = fh.read()
    print(f"The number of words in the file is {counter.number_of_words(text)}")
    print(f"The number of lines in the file is {counter.number_of_lines(text)}")
    print(f"The number of characters in the file is {counter.number_of_characters(text)}")


main()
