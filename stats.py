def get_book_text(file_path: str):
    with open(file_path) as f:
        file_content = f.read()

    return file_content

def count_words(file):
    file_content = file.split()

    return len(file_content)



def char_count(file):
    file_lower = file.lower()

    character_dic = dict()

    for c in file_lower:
        if c in character_dic:
            continue
        else:
            character_dic[c] = file_lower.count(c)
    return character_dic

def sort_the_chars(char_dict):

    chars_list = list()

    for e in char_dict:
         chars_list.append({"char" : e, "num" : char_dict[e]})

    def sort_on(items):
        return items["num"]

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list

    

