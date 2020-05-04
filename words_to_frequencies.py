def words_to_frequencies(words):
    freqs = {}
    for word in words:
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1
        print(freqs)   # for debug
    return freqs


def most_common_words(freqs):
    best = max(freqs.values())
    words = []
    for word, count in freqs.items():
        if count == best:
            words.append(word)

    return (words, best)


words = ['abc', 'abc', 'cba']
# words_to_frequencies(words)
print(most_common_words(words_to_frequencies(words)))