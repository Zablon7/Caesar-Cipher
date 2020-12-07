def rotate_letter(letter, n):
    if letter.islower():
        start = ord('a')
    elif letter.isupper():
        start = ord('A')
    else:
        return letter
    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    result = ''
    for letter in word:
        result += rotate_letter(letter, n)
    return result


letter = input('Enter word: ')
n = int(input('How many times do you want to rotate it? '))
print(rotate_word(letter, n))
