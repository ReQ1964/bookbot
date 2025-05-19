def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict['num']

def get_sorted_chars(chars):
    dicts_list = []
    for c in chars:
        if(c.isalpha()):
            new_dict = {"char": c, "num": chars[c]}
            dicts_list.append(new_dict)
    dicts_list.sort(reverse=True, key=sort_on)
    return dicts_list



