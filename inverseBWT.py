def getSubIndex(text):
    vocab = []
    newString = []
    for char in text:
        if char not in vocab:
           newString.append(char + str(1))
        else:
           newString.append(char + str(vocab.count(char)+1))
        vocab.append(char)
    return newString


def inverseBWT(text):
    firstCol = ''.join(sorted(text))
    
    reconstructedStr = ""
    expandedText = getSubIndex(text)
    expandedFirstCol = getSubIndex(firstCol)    
    print(expandedText)
    currChar = expandedFirstCol[0]
    for k in range(len(text)):
        pos = expandedText.index(currChar)
        currChar = expandedFirstCol[pos]        
        reconstructedStr += currChar[0]
    return reconstructedStr


def main():
   text = "AT$AAACTTCG"
   print inverseBWT(text)

if __name__ == "__main__":
    main()
   
