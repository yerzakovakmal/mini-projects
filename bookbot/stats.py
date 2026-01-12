def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    char_counts = {}
    text = file_contents.lower()
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sorted(dict_item):
    return dict_item["num"]

def sort_char_count(chars_dict):
    chars_list = []

    for char, count in chars_dict.items():
        chars_list.append({"char": char, "num": count})
    chars_list.sort(reverse=True, key=sorted)
    return chars_list