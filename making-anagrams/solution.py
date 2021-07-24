from collections import defaultdict
from string import ascii_lowercase

def makeAnagram(a, b):
    a_letters = defaultdict(int)
    b_letters = defaultdict(int)
    
    for letter in a:
        a_letters[letter] += 1
    for letter in b:
        b_letters[letter] += 1
    
    min_deletions = 0
    for letter in ascii_lowercase:
        min_deletions += abs(a_letters[letter] - b_letters[letter])
    
    return min_deletions

a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

print(makeAnagram(a, b))


