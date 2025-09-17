def get_num_words(book):
    num_words = len(book.split())
    #print(f"{num_words} words found in the document")
    return num_words

def get_num_characters(book):
    characters_dict = {}
    book = book.lower()
    for key in book:
        if key not in characters_dict:
            characters_dict[key] = 1
        else:
            characters_dict[key] = int(characters_dict[key]) + 1
    #print(characters_dict)
    return characters_dict

def sort_on(items):
    return items["num"]

def print_report(num_words, characters_dict, book_path):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    x = list(characters_dict.items()); x.sort(key=lambda x: x[1], reverse=True)
    for key, value in x:
        if key.isalpha():
            print(f"{key}: {value}")
        