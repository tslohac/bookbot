from stats import get_num_words, count_characters, sort_on, dict_to_list

def get_book_text(filepath):
    with open(filepath) as f:
    # do something with f (the file) here
        file_contents = f.read()
        return file_contents
    
# books path
  


def main():
    # import built-in sys module
    import sys
    if len(sys.argv) <2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_path = sys.argv[1]
    the_book = get_book_text(relative_path)             # the book's text
    num_words = get_num_words(the_book)                 # number of all the words in the book

    character_count = count_characters(the_book)        # the original dictionary representing the count of each character in the book
    # print(f"{num_words} words found in the document")
    # print(character_count)
    new_list = dict_to_list(character_count)
    # print(new_list)
    new_list.sort(reverse=True, key=sort_on)
    # print(new_list)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in new_list:
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")
    


main()