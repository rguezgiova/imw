import sys

def num_vowels(text):
    num_vowels = 0
    for char in text.lower():
        if char in 'aeiou':
            num_vowels += 1
    return num_vowels

def num_whitespaces(text):
    num_whitespaces = 0
    for char in text:
        if char in ' ':
            num_whitespaces += 1
    return num_whitespaces

def num_digits(text):
    num_digits = 0
    for char in text:
        if char in '0123456789':
            num_digits += 1
    return num_digits

def num_words(text):
    roster = text.split()
    words = len(roster)
    return words

def reverse(text):
    string = text
    rever = text[::-1]
    return rever

def length(text):
    num_char = len(text)
    return num_char

def halfs(text):
    string_range = len(text)
    if string_range >= 2:
        mid = string_range // 2
        fist_part = text[:mid]
        second_part = text[mid:]
    return " | ".join((fist_part, second_part))

def upper_vowels(text):
    vowels = "AEIOU"
    uppervowels = ""
    for char in text:
        if char.upper() in vowels:
            uppervowels += char.upper()
        else:
            uppervowels += char
    return uppervowels

def sorted_by_words(text):
    roster = text.split()
    roster.sort()
    sort = ' '.join(roster)
    return sort

def length_of_words(text):
    text_roster = text.split()
    size_roster = []
    for char in text_roster:
        size = str(len(char))
        size_roster.append(size)
    word_size = " ".join(size_roster)
    return word_size

if __name__ == '__main__':
    text = sys.argv[1]
    print('Number of vowels:', num_vowels(text))
    print('Number of whitespaces:', num_whitespaces(text))
    print('Number of digits:', num_digits(text))
    print('Number of words:', num_words(text))
    print('Reverse of text:', reverse(text))
    print('Length of text:', length(text))
    print('Halfs of text:', halfs(text))
    print('Text with uppercased vowels:', upper_vowels(text))
    print('Sorted by words:', sorted_by_words(text))
    print('Length of words:', length_of_words(text))
