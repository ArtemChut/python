"""
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".
"""

def wordPattern(pattern, s):
    dict = {}

    values = s.split(" ") # deleting all the spaces between words

    if len(values) != len(pattern): # they cannot be the same if they're different lengths
        return False
    else:
        # making sure neither a letter not a word appeares more than once
        letters_appeared = []
        values_used = []

        for i in range(len(pattern)):
            if (not pattern[i] in letters_appeared) and (not values[i] in values_used):
                print(values[i])
                dict[pattern[i]] = values[i]
            letters_appeared.append(pattern[i])
            values_used.append(values[i])

        num_correct = 0
        for i in range(len(values)):
            for key, value in dict.items():
                if value == values[i]: # comparing the value until the same one is found
                    if key == pattern[i]: # if letter connected to that word is the same then...
                        num_correct += 1

        if num_correct == len(values):
            return True
        return False
print(wordPattern("abba", "cat dog dog cat"))
