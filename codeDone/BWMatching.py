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


def matchingLastToFirst(firstColumn, lastColumn):
   lastToFirst = []
   firstColExp = getSubIndex(firstColumn)
   lastColExp = getSubIndex(lastColumn)
   for ch in lastColExp:
      lastToFirst.append(firstColExp.index(ch))
   return lastToFirst

def BWMatching(firstColumn, lastColumn, pattern, matching):
   top = 0
   bottom = len(lastColumn)-1
   while top <= bottom:
       if len(pattern) > 0:
          symbol = pattern[-1]
          pattern = pattern[0:-1]
          if symbol in lastColumn[top:(bottom+1)]:
             #print(lastColumn[top:(bottom+1)])
             #print "symob is " + symbol
             indices = [i for i, x in enumerate(list(lastColumn[top:(bottom+1)])) if x == symbol]
             topIndex = indices[0] + top 
             bottomIndex = indices[-1] + top
             #print topIndex, bottomIndex
             top = matching[topIndex]
             bottom = matching[bottomIndex]
             #print top, bottom
          else:
             return 0
       else:
          return bottom - top + 1



def main():
   f = open('/Users/tingliu/Downloads/dataset_300_8 (2).txt', 'r')
   text = f.readline().strip()
   firstColumn = ''.join(sorted(text))
   patterns = []
   for l in f:
      patterns = (l.rstrip().split(' '))
   print len(patterns)
   res = []
   matching = matchingLastToFirst(firstColumn, text)
   for i, pattern in enumerate(patterns):
       print i
       res.append(BWMatching(firstColumn, text, pattern, matching))
   print res
   fp =  open('/Users/tingliu/Downloads/res1.txt', 'w')
   for r in res:
      fp.write("%s " % r)
   

if __name__ == "__main__":
    main()
