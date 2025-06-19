from stats import num_words
from stats import get_character_count
from stats import sort_characters

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents   
def print_only_alpha(characters):
    for character in characters:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
def main(book):
    file_contents = get_book_text(book)
    word_count = num_words(file_contents)
    character_count = get_character_count(file_contents)
    sorted_characters = sort_characters(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_only_alpha(sorted_characters)
    print("============= END ===============")

main("books/frankenstein.txt")