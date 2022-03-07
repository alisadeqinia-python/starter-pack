def spin_words(sentence):
    '''
    its spinning words with 5 characters and more
    '''
    words = " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
    return words


A = "hello my friend"
B = spin_words(A)
print(B)
