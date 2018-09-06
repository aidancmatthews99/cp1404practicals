
text = input("Text: ")

words = text.split()
word_to_count = {}
spacer = -1

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
        if spacer < len(word):
            spacer = len(word)

words_without_copies = word_to_count.keys()
words_without_copies = sorted(words_without_copies)

for key in words_without_copies:
    print("{:{}} : {}".format(key, spacer, word_to_count[key]))
