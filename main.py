from stats import *
import sys

def check_arguments():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_arguments()
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    chars = count_chars(book_text)
    sorted_chars = get_sorted_chars(chars)
    print_report(book_path, num_words, sorted_chars)


def print_report(path, num_words, chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in chars_sorted:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()
