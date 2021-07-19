
# will remove the stop words in a string
def remove_stop_words(str, stop_words):
    words = str.split(' ')
    for i in words:
        if i in stop_words:
            words.remove(i)

    str = ''
    for i in words:
        str += i + ' '

    return str
