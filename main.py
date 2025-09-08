from stats import get_book_text, count_words, char_count, sort_the_chars
import sys


def main():
    sys_list = sys.argv

    if len(sys_list) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys_list[1]

    

    file_txt = get_book_text(file_path=file_path)

    word_numbers = count_words(file_txt)

    char_numbers_dict = char_count(file_txt)

    sorted_list_chars = sort_the_chars(char_numbers_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_numbers} total words")
    print("--------- Character Count -------")
    for el in sorted_list_chars:
        if el['char'].isalpha():
            print(f"{el['char']}: {el['num']}")
    print("============= END ===============")


main()
