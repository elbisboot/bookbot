import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import get_num_of_words
from stats import count_characters
from stats import sorted_list_of_dictionaries
filepath = sys.argv[1]
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_of_words(text)} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_list_of_dictionaries(count_characters(text)):
        if char_dict['char'].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")
main()