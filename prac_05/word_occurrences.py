"""
Word Occurrences
Estimate: 30 minutes
Actual:   11 minutes
"""

word_to_count = {}

string = input("Enter a string: ")
words = string.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

longest_word_length = max(len(word) for word in word_to_count.keys())

for word, count in sorted(word_to_count.items()):
    print(f"{word:{longest_word_length}} : {count}")
