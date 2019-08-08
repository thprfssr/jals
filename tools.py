#!/bin/python

import sys # For the sys.exit() function

# Here we define various sets of characters that we'll be using often
MINUSCULE_LATIN_ALPHABET = "abgdeθijklmnoprstuwφx"
MAJUSCULE_LATIN_ALPHABET = "ABGDEΘIJKLMNOPRSTUWΦX"
MINUSCULE_LATIN_SHORT_VOWELS = "aeiou"
MINUSCULE_LATIN_LONG_VOWELS = "āēīōū"
MAJUSCULE_LATIN_SHORT_VOWELS = "AEIOU"
MAJUSCULE_LATIN_LONG_VOWELS = "ĀĒĪŌŪ"
MISCELLANEOUS = " -"
MINUSCULE_CYRILLIC_ALPHABET = "абгдеѳийклмнопрстуўфх"
MAJUSCULE_CYRILLIC_ALPHABET = "АБГДЕѲИЙКЛМНОПРСТУЎФХ"
MINUSCULE_CYRILLIC_SHORT_VOWELS = "аеиоу"
MAJUSCULE_CYRILLIC_SHORT_VOWELS = "АЕИОУ"
MACRON = "\u0304"
COLON = ":"



# This function accepts a Danetian word as an argument, and converts it into a
# format which is easier to deal with when alphabetizing. Capital letters get
# minusculized, and macrons get converted into colons. If the word contains a
# character which is not in the allowed characters, then the program dies.
#
# This function accepts an optional 'colons' flag, with a default value of
# True. In the case that it's set to False, then the returned sanitized word
# will have all colons removed.
#
# The function assumes that the given word has all its macronated vowels as a
# single unicode character, rather than a character plus the separate \u0304
# macron character. Moreover, we assume that the given word is written in the
# Danetian Latin script, rather than the Cyrillic script.
def sanitize(word, *args, **kwargs):
    colons = kwargs.get("colons", True)

    n = len(word)
    sanitized_word = ""
    for char in word:
        c = ""
        # We use this conditional in order to transform each character. Once
        # we have the transformed character c, then we append it to the
        # sanitized_word string.
        if char in MINUSCULE_LATIN_LONG_VOWELS:
            i = MINUSCULE_LATIN_LONG_VOWELS.index(char)
            c = MINUSCULE_LATIN_SHORT_VOWELS[i] + (COLON if colons else "")
        elif char in MAJUSCULE_LATIN_LONG_VOWELS:
            i = MAJUSCULE_LATIN_LONG_VOWELS.index(char)
            c = MINUSCULE_LATIN_SHORT_VOWELS[i] + (COLON if colons else "")
        elif char in MINUSCULE_LATIN_ALPHABET:
            i = MINUSCULE_LATIN_ALPHABET.index(char)
            c = MINUSCULE_LATIN_ALPHABET[i]
        elif char in MAJUSCULE_LATIN_ALPHABET:
            i = MAJUSCULE_LATIN_ALPHABET.index(char)
            c = MINUSCULE_LATIN_ALPHABET[i]
        elif char in MISCELLANEOUS:
            c = ""
        else:
            # If char isn't in any of the alphabets we checked, then die.
            print("Error in sanitize():")
            print("Illegal word:", word)
            print("Character not allowed in Danetian:", char)
            sys.exit(-1)

        # Append the transformed character c to the sanitized_word string.
        sanitized_word += c

    return sanitized_word
