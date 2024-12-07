def add_definition(dictionary, word, definition):
    dictionary[word] = dictionary.get(word, []) + [definition]
    return len(dictionary[word])

def remove_word(dictionary, word):
    if word in dictionary:
        del dictionary[word]
        return True
    return False

def remove_definition(dictionary, word, index):
    if word in dictionary and index < len(dictionary[word]):
        dictionary[word].pop(index)
        return True
    return False

def lookup(dictionary, word):
    if word in dictionary:
        return dictionary[word]
    return ''

