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
             print (i, t, currNodeNum)
          else:
             initial = False
             nodes[(currNodeNum, t)] = allnodeCounter
             if allnodeCounter == 184:
                print (currNodeNum, t, allnodeCounter)
                print (183, 'A') in nodes
             currNodeNum = allnodeCounter
             allnodeCounter += 1
    return nodes

def prefixTrieMatching(text, patterns):
   nodes = trieConstruction(patterns)
   symbol = text[0]
   while true:
      if 
   
      