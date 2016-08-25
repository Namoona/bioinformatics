import numpy as np
def SuffixArray(text, K):
   suffixArray = []
   for i in range(0,len(text)):
         suf = text[(len(text)-i-1):]
         suffixArray.append((suf, (len(text)-i-1)))
   partialSuffixArray = {}
   for s, i in enumerate(sorted(suffixArray)):
      if i[1] % K == 0:
       partialSuffixArray[s] == i[1] 
   return partialSuffixArray

def BWTmatrix(text):
   allBWT = [text]
   for i in range(1,len(text)):
      allBWT.append(text[i:] +text[0:i])
   return allBWT

def BWT(text):
    toStore = ""
    BWTmat = BWTmatrix(text)
    for t in sorted(BWTmat):
        toStore = toStore +t[-1]
    return toStore

def betterBWMatchingWithCheckpoint(firstOccurrence,lastCol, pattern, checkpointMatrix, modulus):
   top = 0
   bottom = len(lastCol)-1
   while top <= bottom:
      if len(pattern) > 0:
         symbol = pattern[-1]
         pattern = pattern[0:-1]
         if symbol in lastCol[top:(bottom+1)]:
             top = firstOccurrence[symbol] + count(symbol, top, lastCol, checkpointMatrix, modulus)
             bottom = firstOccurrence[symbol] + count(symbol, bottom+1, lastCol, checkpointMatrix, modulus) - 1
             print "top " + str(top)
             print "bottom " + str(bottom)
         else:
             return 0
      else:
         return (top, bottom)

def findAllPos(top, bottom, sa):
    allpos = []
    for ind in top:(bottom+1):
       if ind in sa:
           allpos.append(sa[ind])
       else:
           


def findFirstOccurrence(firstColumn):
    firstOccurrence = {}
    symbols = list(set(firstColumn))
    for symbol in symbols:
       firstOccurrence[symbol] = firstColumn.find(symbol)
    return firstOccurrence

def buildCheckpointCountMatrix(lastColumn, modulus):
    length = int(len(lastColumn) / modulus)
    uniqueVocab = list(set(lastColumn))
    checkpointCountMatrix = []
    checkpointCountMatrix.append([0] * len(uniqueVocab))
    for i in range(length):
        countVec = []
        for uv in uniqueVocab:
            countVec.append(lastColumn[0:((i+1)*5)].count(uv))
        checkpointCountMatrix.append(countVec)
    return checkpointCountMatrix

def count(symbol, top, lastColumn, checkpointMatrix, modulus):
    uniqueVocab = list(set(lastColumn))
    cpc = checkpointMatrix[int(top/modulus)][uniqueVocab.index(symbol)]
    aftercpcStr = lastColumn[(int(top/modulus) * modulus):(top)]
    aftercpc = aftercpcStr.count(symbol)
    #print "count is " + str(aftercpc + cpc)
    return aftercpc + cpc


def main():
    f = open('/Users/tingliu/Downloads/test.txt', 'r')
    text1 = f.readline().strip()+"$"
    text = BWT(text1)
    firstColumn = ''.join(sorted(text))
    patterns = []
    for l in f:
      patterns.append(l.rstrip())
    print len(patterns)
    firstOccurrence = findFirstOccurrence(firstColumn)
    modulus = 5
    sa = SuffixArray(text, modulus)
    checkpointCountMatrix = buildCheckpointCountMatrix(text, modulus)
    print checkpointCountMatrix
    res = []
    for i, pattern in enumerate(patterns):
        print i
        top, bottom = betterBWMatchingWithCheckpoint(firstOccurrence, text, pattern, checkpointCountMatrix, modulus)
        for ind in top:(bottom+1):
           if ind in sa:
               allpos.append(sa[ind])
           else:



    print res
    fp =  open('/Users/tingliu/Downloads/res2.txt', 'w')
    for r in res:
      fp.write("%s " % r)
        

if __name__ == "__main__":
    main()