sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.split()

selected_indices = [1, 5, 6, 7, 8, 9, 15, 16, 19]
word_positions = {}

for index, word in enumerate(words, 1):
    if index in selected_indices:
        word_positions[word[0]] = index
    else:
        word_positions[word[:2]] = index

print(word_positions)
