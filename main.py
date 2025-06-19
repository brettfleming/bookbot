from stats import num_words


def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents   

def main(book):
    file_contents = get_book_text(book)
    word_count = num_words(file_contents)
    print(f"{word_count} words found in the document")

main("books/frankenstein.txt")