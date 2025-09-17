from sys import argv
from stats import *

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        book_contents = get_book_text(argv[1])
        num_words = get_num_words(book_contents)
        characters_dict = get_num_characters(book_contents)
        print_report(num_words, characters_dict, argv[1])

if __name__ == '__main__':
    main()