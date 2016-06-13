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

def main():
   patterns = []
   fn = open('/Users/tingliu/Downloads/dataset_294_4 (4).txt', 'r')
   for l in fn:
      patterns.append(l.rstrip())
   nodes = trieConstruction(patterns)

   import csv
   with open('test1.txt', 'w') as fp:
      for key, val in nodes.iteritems():
         s, b = key
         data = str(s)+ "->"+ str(val)+":"+b+"\n"
         fp.write(data)

if __name__ == "__main__":
    main()