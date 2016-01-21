# coding: utf-8
import re
def spoonerize(word1, word2):
    vowels = "[aeiou]"
    a, b = re.split(vowels, word1)[0], re.split(vowels, word2)[0]
    return b+word1[len(a):], a+word2[len(b):]
