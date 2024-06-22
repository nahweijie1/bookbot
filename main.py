def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char_dict = get_character_counts(text)
    print(f"{num_words} words found in the document")
    print(f'{len(num_char_dict)} distinct characters found in the document: ')
    for k, v in num_char_dict.items():
        print(f"{k}: {v}")


def get_num_words(text):
    '''Takes in a string `text` and returns the number of words within `text` as an `int`'''
    words = text.split()
    return len(words)


def get_book_text(path):
    '''Takes in a string `path` to a file, calls `open()` on the file and returns the content of the file as a `string` using `read()`'''
    with open(path) as f:
        return f.read()

def get_character_counts(text):
    '''Takes in a string `text` and returns the count of each character as a `dict` with a key: value pair of `'character': count` of type `string: int`
        * Note: This method does not take into account case sensitivity as `.lower()` is called on text before performing character count. '''
    character_dict = {}
    for char in text.lower():
        if char not in character_dict:
            character_dict.update({char: 1})
        else:
            character_dict[char] += 1
    return character_dict

main()