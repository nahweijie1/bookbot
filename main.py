def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_counts(text):
    character_dict = {}
    for char in text.lower():
        if char not in character_dict:
            character_dict.update({char: 1})
        else:
            character_dict[char] += 1
    return character_dict

def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for k, v in dict.items():
        sorted_list.append({'char': k, 'count': v})
    return sorted_list

def sort_on(dict):
    return dict['count']

def generate_report_header(text):
        print(f"--- Begin report of {text} ---")
    
def generate_report_footer():
        print(f"--- End report ---")
    
def generate_report(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char_dict = get_character_counts(text)
    characters = chars_dict_to_sorted_list(num_char_dict)
    characters.sort(reverse = True, key=sort_on)
    
    generate_report_header(book_path)
    print(f"{num_words} words found in {book_path}")
    print("")
    for item in characters:
        if not item['char'].isalpha():
            continue
        print(f" The '{item['char']}' character was found {item['count']} times")
    generate_report_footer()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    key_list = ['char','count']
    generate_report(book_path)

main()