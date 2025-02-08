def count_word_occurrences(text):
    word_counts = {}
    words = text.lower().split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

text = "rose beli rose lily dalia rose beli"
print(count_word_occurrences(text)) 

