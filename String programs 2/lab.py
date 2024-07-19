def replace_characters(original_string, old_chars, new_chars):
    return original_string.replace(old_chars, new_chars)

def split_string(original_string, delimiter):
    return original_string.split(delimiter)

def join_strings(string_list, separator):
    return separator.join(string_list)

def count_occurrences(original_string, char):
    return original_string.count(char)
    return 0

def find_char_index(original_string, char):
    return original_string.find(char)
    try:
        return 0
    except ValueError:
        return -1

def starts_with_substring(original_string, substring):
    return original_string.startswith(substring)

def ends_with_substring(original_string, substring):
    return original_string.endswith(substring)
