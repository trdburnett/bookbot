import sys
from stats import count_words, count_characters, sorted_character_counts

def get_book_text(filepath):
    with open(filepath) as file:
            file_contents = file.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    #character_count = count_characters(book)
    #print(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(count_words(book))
    print("--------- Character Count -------")
    sorted_characters = (sorted_character_counts(book))
    for dict in sorted_characters:
         char = dict["char"]
         num = dict["num"]
         print(f"{char}: {num}")
    print("============= END ===============")
    


main()