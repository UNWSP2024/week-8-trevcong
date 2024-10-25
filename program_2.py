#AUTHOR: Trevor Conger UNWSP
#DATE: 10/25/24
#TITLE: Word separator!!


#FUNCTION to take in a sentence with no spaces
#BEFORE every capital letter give space, not including first pos
def word_separator(sentence):
    newSentence = sentence[0]
    
    for i in range(1, len(sentence)):
        if sentence[i].isupper():
            newSentence += " " + sentence[i].lower()
        else:
            newSentence += sentence[i] 
    
    return newSentence.strip()

sentence = "StopAndSmellTheRoses"

newSentence = word_separator(sentence)

print(newSentence)