def num_words(file):
    words = file.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count 

def get_character_count(file):
    words = file.split()
    characters = {}
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in characters:
                characters[letter] += 1   
            else: characters[letter] = 1     
    return print(characters)