def scrambleWord(word):
    current = 0
    result=''
    while(current<len(word)-1):
        if word[current:current+1]==('A') and word[current+1:current+2]!=('A'):
            result = result + word[current+1:current+2]
            result = result + 'A'
            current = current + 2
        else:
            result = result + word[current:current+1]
            current = current + 1
    if (current<len(word)):
        result = result + word[current]
    return result
def scrambleOrRemove(wordList):
    index = 0
    length = len(wordList)
    while index<len(wordList):
        word = wordList[index]
        scrambled=scrambleWord(word)
        if(word==scrambled):
            wordList.remove(word)
            index=index-1
            length=length-1
        else:
            index=index+1
print(scrambleWord('ANA'))
print(scrambleWord('APPLE'))
print(scrambleWord('ABRACDABRA'))
print(scrambleWord('WHOL'))
print(scrambleWord('EGGS'))
aList = ['ANA','APPLE','ABRACDABRA',"WHOL",'EGGS']
scrambleOrRemove(aList)
print(aList)