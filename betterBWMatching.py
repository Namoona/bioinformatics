def count(symbol, top, lastColumn):
   return lastColumn[0:top].count(symbol)



def betterBWMatching(firstOccurrence,lastCol, pattern):
   top = 0
   bottom = len(lastCol)-1
   while top <= bottom:
      if len(pattern) > 0:
         symbol = pattern[-1]
         pattern = pattern[0:-1]
         if symbol in lastCol[top:(bottom+1)]:
             top = firstOccurrence[symbol] + count(symbol, top, lastCol)
             bottom = firstOccurrence[symbol] + count(symbol, bottom+1, lastCol) - 1
             #print "top " + str(top)
             #print "bottom " + str(bottom)
         else:
             return 0
      else:
         return bottom - top + 1   

def findFirstOccurrence(firstColumn):
    firstOccurrence = {}
    symbols = list(set(firstColumn))
    for symbol in symbols:
       firstOccurrence[symbol] = firstColumn.find(symbol)
    return firstOccurrence


def main():
    f = open('/Users/tingliu/Downloads/dataset_303_4 (1).txt', 'r')
    text = f.readline().strip()
    firstColumn = ''.join(sorted(text))
    for l in f:
      patterns = (l.rstrip().split(' '))
    print len(patterns)
    firstOccurrence = findFirstOccurrence(firstColumn)

    res = []
    for i, pattern in enumerate(patterns):
        print i
        res.append(betterBWMatching(firstOccurrence, text, pattern))
    print res
    fp =  open('/Users/tingliu/Downloads/res2.txt', 'w')
    for r in res:
      fp.write("%s " % r)
        

if __name__ == "__main__":
    main()