from typing import Dict
import string


def str_for_dct(text: str) -> Dict[str, int]:
    dct = {}
    for position, i in enumerate(text):
        if i in dct:
            dct[i] += [position]
        else:
            dct[i] = [position]
        
    return dct


valid_letters = string.ascii_uppercase
used_letters = []

# word = input("Give me a word: ").upper()
word = "TEST"
word_dct = str_for_dct(word)
shadow = ["_" for i in range(len(word))]


while "_" in shadow:
    print(shadow)
    letter = input("Give me a letter: ").upper()

    if letter in word and letter in valid_letters:
        used_letters.append(letter)
        for i in word_dct.get(letter):
            shadow[i] = letter
    else:
        print(f"The {letter} isn`t in the word")

print(f"Congratulations! The word is {word}")
