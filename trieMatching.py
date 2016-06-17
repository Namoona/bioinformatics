import sys
def trieConstruction(patterns):
    nodes = {}
    allnodeCounter = 1
    for pattern in patterns:
       initial = True
       currNodeNum = 0
       for i, t in enumerate(pattern):
          if((currNodeNum, t) in nodes) & initial:
             currNodeNum = nodes[(currNodeNum,t)]
          else:
             initial = False
             nodes[(currNodeNum, t)] = allnodeCounter
             currNodeNum = allnodeCounter
             allnodeCounter += 1
             # print(i)
             # print(len(pattern))
             if (i+1) == len(pattern):
                # print("leaf")
                nodes[(currNodeNum, '$')] = str(currNodeNum) + '$'
    return nodes

def prefixTrieMatching(text, trie):
   nodes = trie
   curSymbolCounter = 0
   v = 0
   path = ''
   while curSymbolCounter < (len(text)+1):
      if (v,'$') in nodes:
         print("match")
         return path
      if (curSymbolCounter < len(text)):
         symbol = text[curSymbolCounter]
         if ((v,symbol) in nodes) & (curSymbolCounter < len(text)):
            # print(v)
            # print(symbol)
            # print(nodes[(v,symbol)])
            v = nodes[(v,symbol)]
            path = path + symbol
            # print(path)
            curSymbolCounter += 1
            # print(curSymbolCounter)
            # print(text)
         else:
            # print("no matches found")
            return
      else:
          return
      


def trieMatching(text, trie):
   nodes = trie
   pos = []
   counter = 0
   while len(text) >0:
      m = prefixTrieMatching(text, trie)
      if(m != None):
         # print(m)
         print(counter)
         pos.append(counter)
      counter +=1
      text = text[1:]
   return pos


def main():
   patterns = []
   f = open('/Users/tingliu/Downloads/dataset_294_8.txt', 'r')
   text = f.readline().strip()
   patterns = []
   for l in f:
      patterns.append(l.rstrip())
   nodes = trieConstruction(patterns)

   pos = trieMatching(text, nodes)
   print pos


if __name__ == "__main__":
    main()      