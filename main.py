path_to_file = "books/frankenstein.txt"

def count_words(text):
    words = text.split()
    print(f' Given text has {len(words)} words.')
    return len(words)

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        
    count_words(file_contents)
    
main()

    
    