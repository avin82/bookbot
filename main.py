import sys
from stats import get_num_words, get_char_count, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content_as_string = get_book_text(sys.argv[1])
    num_words = get_num_words(content_as_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    unsorted_dict = get_char_count(content_as_string)
    sorted_dict_list = sort_dict(unsorted_dict)
    for dict_element in sorted_dict_list:
        for key in dict_element.keys():
            if key.isalpha() and key != "count":
                char_count = dict_element["count"]
                print(f"{key}: {char_count}")
    print("============= END ===============")

main()
