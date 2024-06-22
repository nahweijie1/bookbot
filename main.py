def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    '''Takes in a string `text` and returns the number of words within `text` as an `int`'''
    words = text.split()
    return len(words)


def get_book_text(path):
    '''Takes in a string `path` to a file, calls `open()` on the file and returns the content of the file as a `string` using `read()`'''
    with open(path) as f:
        return f.read()


main()