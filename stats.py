def num_words(file):
    words = file.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count