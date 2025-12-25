def count_words(book):
    words = book.split()
    word_count = len(words)
    result = f"Found {word_count} total words"
    return result

def find_unique_characters(book):
    words = book.split()
    unique_characters = set()
    for word in words:
        for character in word:
            unique_characters.add(character.lower())
    return unique_characters

def count_characters(book):
    unique_characters = find_unique_characters(book)
    count_dict = {}
    for character in unique_characters:
        count_dict[character.lower()] = 0
    words = book.split()
    for word in words:
        for character in word:
            count_dict[character.lower()] += 1
    return count_dict

"""
Better way of doing the above

from collections import Counter

def count_characters(book):
    return Counter(book.lower())

could also count words

def count_words(book):
    words = book.lower().split()
    return Counter(words)

note this would not give a word count as above. Instead it would return a dict of each occurance of a word

"""

def sort_on(items):
    return items["num"]

def sorted_character_counts(book):
    character_dict = count_characters(book)
    character_list = []
    for key in character_dict:
        if key.isalpha():
            character_list.append({"char": key, "num": character_dict[key]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list
    
