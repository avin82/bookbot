def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()]+= 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def sort_dict(unsorted_dict):
    list_char_count = []
    for key in unsorted_dict.keys():
        list_char_count.append({f"{key}": key, "count": unsorted_dict[key]})
    list_char_count.sort(reverse=True, key=sort_on)
    return list_char_count