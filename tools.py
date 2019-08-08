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

# This function is a <= relation between two Danetian words. The function
# sanitizes the pair of words, so the words must be passed unsanitized.
def total_order(word_a, word_b):
    # We sanitize the pair of words, ignoring colons for now.
    ua = sanitize(word_a, colons = False)
    ub = sanitize(word_b, colons = False)

    # We are gonna check letter by letter, up to the length of the
    # smallest word.
    na = len(ua)
    nb = len(ub)
    n = min(na, nb)
    alphabet = MINUSCULE_LATIN_ALPHABET
    for k in range(0, n):
        # Go letter by letter, from the beginning of each word. The moment we
        # find a pair of letters which are not equal, then we know that one
        # word is greater than the other.
        ca = ua[k]
        cb = ub[k]
        i = alphabet.index(ca)
        j = alphabet.index(cb)

        # Exit the function if we find a pair of letters which are not equal.
        if i < j:
            return True
        if i > j:
            return False

    # If the function hasn't exited yet, then it means that all the letters
    # that we checked are identical. We checked all the letters up to the
    # length of the smallest word. Hence, if the function still hasn't exited,
    # this means that the two words have identical letters up to the length of
    # the smallest word. Hence, it's possible that one word is longer than
    # the other. The shorter word goes before the longer word.
    if na < nb:
        return True
    if na > nb:
        return False

    # If the function still hasn't exited, then the two words have exactly the
    # same length, and exactly the same letters. We must now pay attention to
    # the placement of the macrons. I want to emulate the following order:
    # aka
    # akā
    # āka
    # ākā
    # So we look at the first letter. If one has a macron and the other does
    # not, then the unmacronated word goes before the macronated word.
    # Otherwise, we look at the following letter.
    #
    # First we sanitize the original words, but now we include the colons
    # (which are transformed from original macrons):
    ua = sanitize(word_a, colons = True)
    ub = sanitize(word_b, colons = True)
    na = len(ua)
    nb = len(ub)
    n = min(na, nb)
    for k in range(0, n):
        # Fetch the characters from the strings ua and ub
        ca = ua[k]
        cb = ub[k]

        if ca == cb:
            continue
        elif ca != COLON and cb == COLON:
            return True
        elif ca == COLON and cb != COLON:
            return False

    # By this point, if the function hasn't exited, then the two words are
    # of the same length, have the same characters, and have the same placement
    # of macrons. Then, they can only differ in the placement of spaces and
    # dashes. At the moment of writing this function, no importance is given
    # to this. Hence, "akapara", "aka para", and "aka-para" are all identical.
    # In order to make this function a total order, rather than a strict total
    # order, we return True.
    return True
