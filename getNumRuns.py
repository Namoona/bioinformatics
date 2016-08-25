def getNumRuns(text):
    allpairs = []
    for i in range(len(text)-1):
        allpairs.append(text[i+1]+text[i])
    allpairs.append(text[0]+ text[len(text)-1])
    lastPos = ""
    print(sorted(allpairs))
    for k in sorted(allpairs):
        lastPos += k[1]
    return lastPos
    
def main():
    text = "panamabananas$"
    f = open('/Users/tingliu/Downloads/E-coli.txt', 'r')
    text = f.readline().strip()
    lastPos = getNumRuns(text)
    print(lastPos)


if __name__ == "__main__":
    main()