"""
CP1404/CP5632 Practical - Suggested Solution
Count word occurrences in a string
This example is in the lecture notes 3 different ways
"""

words_to_count = {}
user_text = input("Text: ")
words = user_text.split()
for word in words:
    appearance = words_to_count.get(word, 0)
    words_to_count[word] = appearance + 1

print(words)
words = list(words_to_count.keys())
print(words)
words.sort()

max_words = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_words, words_to_count[word]))
