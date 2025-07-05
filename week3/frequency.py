i={}

def word_frequency(sentence):
    for char in sentence:
        if char in i:
            
            i[char] +=1
        else :
            count=1;
            i[char]= 1
    return i

sentence ="hello"
print(word_frequency(sentence))

