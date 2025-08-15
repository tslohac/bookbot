def get_num_words(book_string):
    list_of_words = book_string.split()
    return len(list_of_words)


def count_characters(book_string):

    char_dict = {}
    for char in book_string.lower():
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict:
            char_dict[char] +=1
    return char_dict

def sort_on(dicts):
    return dicts["num"]
    

def dict_to_list(my_dict):
    the_list = []
    for k,v in my_dict.items():
        if k.isalpha():
            the_list.append({"char": k, "num": v})
    return the_list
    