def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    num_words = num_of_words(text) 
    total_chars = count_chars(text) 

    print("--- Begin report of books/frankenstein.txt")

    print(f"There are {num_words} in the frankenstein text.")


    total_chars =  dict(sorted(total_chars.items(), reverse=True, key=lambda item: item[1]))

    for letter in total_chars:
        if letter.isalpha():
            print(f"The character {letter} is appered in the text {total_chars[letter]} times")

    print("---End of the report---")

def num_of_words(text):
    text_list = text.split()
    return len(text_list)


def count_chars(text):
    char_dct = dict()
    for letter in text:
        letter = letter.lower()
        if letter in char_dct:
            char_dct[letter] += 1
        else:
            char_dct[letter] = 1
    return char_dct


def read_book(book_path):
    with open(book_path) as f:
        return f.read()

main()