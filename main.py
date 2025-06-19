def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return print(file_contents), file_contents   

def main(book):
    get_book_text(book)

main("books/frankenstein.txt")