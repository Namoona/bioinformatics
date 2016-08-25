from __future__ import division

def findWhichColumn2Remove(threshold, ml):
   colNum = []
   #print ml[0]
   #print "length is " + str(len(ml[0]))
   for i in range(len(ml[0])):
      col = []
      for l in ml:
         col.append(l[i])
      if col.count("-")/len(ml) < threshold:
         colNum.append(i)
   return colNum

def buildDictionary(colNum, ml):
   transitionMap = {("S", 0, "M", 1) : 0, ("S", 0, "I", 0) : 0, ("S", 0, "D", 1) : 0, ("I", 0, "M", 1) : 0, ("I", 0, "I", 0) : 0, ("I", 0, "D", 1) : 0}
   transitionSum = {("S", 0) : 0, ("I", 0) : 0}
   
   #print "colnum is " + str(colNum)
   for i, cn in enumerate(colNum):
      if(i+1 < len(colNum)):
         transitionMap[("M", i+1, "I", i+1)] = 0
         transitionMap[("M", i+1, "M", i+2)] = 0
         transitionMap[("M", i+1, "D", i+2)] = 0
         transitionMap[("D", i+1, "I", i+1)] = 0
         transitionMap[("D", i+1, "M", i+2)] = 0
         transitionMap[("D", i+1, "D", i+2)] = 0
         transitionMap[("I", i+1, "I", i+1)] = 0
         transitionMap[("I", i+1, "M", i+2)] = 0
         transitionMap[("I", i+1, "D", i+2)] = 0
         transitionSum["M", i+1] = 0
         transitionSum["D", i+1] = 0
         transitionSum["I", i+1] = 0
  
   print sorted(transitionMap.keys())      
   for i,l in enumerate(ml):
      if (0 in colNum):
          if l[0] == "-":
             transitionMap[("S", 0,  "D", 1)] += 1
             transitionSum[("S", 0)] += 1
          else:
             transitionMap[("S", 0, "M", 1)] += 1
             transitionSum[("S", 0)] += 1
      else:
          if l[0] == "-":
             transitionMap[("S", 0,  "M", 1)] += 1
             transitionSum[("S", 0)] += 1
          else:
             transitionMap[("S", 0, "I", 0)] += 1
             transitionSum[("S", 0)] += 1
             if l[1] == "-":
                transitionMap[("I", 0,  "D", 1)] += 1
             else:
                transitionMap[("I", 0,  "M", 1)] += 1
             transitionSum[("I", 0)] += 1
      for j in range(0, len(colNum)-1):
          diff = colNum[j+1] - colNum[j]
          currentChar = l[colNum[j]]
          nextChar = l[colNum[j+1]]
          substrInsert = l[colNum[j]+1 : colNum[j+1]]
          insertNum = substrInsert.count("-")
          if((diff == 1) | ( (diff > 1) & ((insertNum+1) == diff))):
              if currentChar == "-":
                 transitionSum[("D", j+1)] += 1
                 if nextChar == "-":
                    transitionMap[("D", j+1,  "D", j+2)] += 1
                 else:
                    transitionMap[("D", j+1,  "M", j+2)] += 1
              else:
                 transitionSum[("M", j+1)] += 1
                 if nextChar == "-":
                    transitionMap[("M", j+1,  "D", j+2)] += 1
                 else:
                    transitionMap[("M", j+1,  "M", j+2)] += 1
          elif((insertNum+1) < diff):
              transitionMap[("I", j+1,  "I", j+1)] += (len(substrInsert) - insertNum-1)
              transitionSum[("I", j+1)] += (len(substrInsert) - insertNum-1)
              if currentChar =="-":
                 transitionMap[("D", j+1,  "I", j+1)] +=1
                 transitionSum[("D", j+1)] += 1
              else:
                 transitionMap[("M", j+1,  "I", j+1)] +=1
                 transitionSum[("M", j+1)] += 1
              if nextChar == "-":
                 transitionMap[("I", j+1,  "D", j+2)] += 1
                 transitionSum[("I", j+1)] += 1
              else:
                 transitionMap[("I", j+1,  "M", j+2)] += 1
                 transitionSum[("I", j+1)] += 1
          else:
                 print "abc"
   return (transitionMap, transitionSum)


def generateTransitionMatrix(threshold, alphabet, ml, colNum):
   transitionMap, transitionSum = buildDictionary(colNum, ml)
   # for tram in sorted(transitionSum.keys()):
   #    print(tram)
   #    print(transitionSum.get(tram))
   tmColNum = (len(colNum))*3 + 3
   print "tmColNum is " + str(tmColNum)
   transitionMatrix = [[0  for i in range(tmColNum)] for j in range(tmColNum)]
   transitionMatrix[0][2] = transitionMap.get(("S", 0, "M", 1), 0)/transitionSum.get(("S", 0), 0)
   transitionMatrix[0][3] = transitionMap.get(("S", 0, "D", 1), 0)/transitionSum.get(("S", 0), 0)
   transitionMatrix[0][1] = transitionMap.get(("S", 0, "I", 0), 0)/transitionSum.get(("S", 0), 0)
   for key, val in transitionMap.iteritems():
      fromind = -1
      #print "key is " + str(key)
      if (key[0] == "M"):
         fromind = 3*(key[1]-1)+2
      elif (key[0] == "D"):
         fromind = 3*(key[1])
      elif (key[0]=="I"):
         fromind = 3*(key[1])+1
      else:
         fromind = -1
      if fromind>0:   
         ts = transitionSum.get((key[0], key[1]), 0)
         if(ts > 0):
            actualFrac = (val)/(ts)
            if(key[2] == "M"):
               transitionMatrix[fromind][3*key[1]+2] = actualFrac
            elif(key[2] == "D"):
               transitionMatrix[fromind][3*key[1]+3] = actualFrac
            elif(key[2] == "I"):
               transitionMatrix[fromind][3*(key[1])+1] = actualFrac
   transitionMatrix = [row[0:len(transitionMatrix)-3] for row in transitionMatrix[0:len(transitionMatrix)-3]]
   return transitionMatrix

def addPseudocount2TransitionMatrix(transitionMatrix, pseudocount, cn):
   tmColNum = (cn-1)*3 + 3
   pseudoTM = [[0  for i in range(tmColNum)] for j in range(tmColNum)]

   pseudoTM[0][1] = (transitionMatrix[0][1] + pseudocount)/(sum(transitionMatrix[0])+ pseudocount*3)
   pseudoTM[0][2] = (transitionMatrix[0][2] + pseudocount)/(sum(transitionMatrix[0])+ pseudocount*3)
   pseudoTM[0][3] = (transitionMatrix[0][3] + pseudocount)/(sum(transitionMatrix[0])+ pseudocount*3)

   pseudoTM[1][1] = (transitionMatrix[1][1] + pseudocount)/(sum(transitionMatrix[1])+ pseudocount*3)
   pseudoTM[1][2] = (transitionMatrix[1][2] + pseudocount)/(sum(transitionMatrix[1])+ pseudocount*3)
   pseudoTM[1][3] = (transitionMatrix[1][3] + pseudocount)/(sum(transitionMatrix[1])+ pseudocount*3)


   for i in range(1, cn-1):
      pseudoTM[3*i-1][i*3+1] = (transitionMatrix[3*i-1][i*3+1] + pseudocount) / (sum(transitionMatrix[3*i-1]) + pseudocount*3)
      pseudoTM[3*i-1][i*3+2] = (transitionMatrix[3*i-1][i*3+2] + pseudocount) / (sum(transitionMatrix[3*i-1]) + pseudocount*3)
      pseudoTM[3*i-1][i*3+3] = (transitionMatrix[3*i-1][i*3+3] + pseudocount) / (sum(transitionMatrix[3*i-1]) + pseudocount*3)
      
      pseudoTM[3*i][3*i+1] = (transitionMatrix[3*i][3*i+1] + pseudocount) / (sum(transitionMatrix[3*i]) + pseudocount*3)
      pseudoTM[3*i][3*i+2] = (transitionMatrix[3*i][3*i+2] + pseudocount) / (sum(transitionMatrix[3*i]) + pseudocount*3)
      pseudoTM[3*i][3*i+3] = (transitionMatrix[3*i][3*i+3] + pseudocount) / (sum(transitionMatrix[3*i]) + pseudocount*3)
      
      pseudoTM[3*i+1][3*i+1] = (transitionMatrix[3*i+1][3*i+1] + pseudocount) / (sum(transitionMatrix[3*i+1]) + pseudocount*3)
      pseudoTM[3*i+1][3*i+2] = (transitionMatrix[3*i+1][3*i+2] + pseudocount) / (sum(transitionMatrix[3*i+1]) + pseudocount*3)
      pseudoTM[3*i+1][3*i+3] = (transitionMatrix[3*i+1][3*i+3] + pseudocount) / (sum(transitionMatrix[3*i+1]) + pseudocount*3)
   print pseudoTM
   i= (cn-1)
   pseudoTM[3*i-1][i*3+1] = (transitionMatrix[3*i-1][i*3+1] + pseudocount) / (sum(transitionMatrix[3*i-1]) + pseudocount*2)
   pseudoTM[3*i-1][i*3+2] = (transitionMatrix[3*i-1][i*3+2] + pseudocount) / (sum(transitionMatrix[3*i-1]) + pseudocount*2)
   pseudoTM[3*i][3*i+1] = (transitionMatrix[3*i][3*i+1] + pseudocount) / (sum(transitionMatrix[3*i]) + pseudocount*2)
   pseudoTM[3*i][3*i+2] = (transitionMatrix[3*i][3*i+2] + pseudocount) / (sum(transitionMatrix[3*i]) + pseudocount*2)
   pseudoTM[3*i+1][3*i+1] = (transitionMatrix[3*i+1][3*i+1] + pseudocount) / (sum(transitionMatrix[3*i+1]) + pseudocount*2)
   pseudoTM[3*i+1][3*i+2] = (transitionMatrix[3*i+1][3*i+2] + pseudocount) / (sum(transitionMatrix[3*i+1]) + pseudocount*2)

   print pseudoTM
   return pseudoTM

def generateEmissionMatrix(threshold, alphabet, ml, colNum, pseudocount):
   ml1 = ml
   for l in ml1:
      l.pop()
   print ml1
   tmColNum = (len(colNum)-1)*3 + 3
   emissionMatrix = [[0  for i in range(len(alphabet)) ] for j in range(tmColNum)]
   for l in ml1:
      i = 0
      counter = 0
      print l
      for i in range(0,len(l)):
         if (i in colNum):
            if( l[i] != "-"):
               print "letter is " + l[i]
               print str(alphabet.index(l[i]))
               emissionMatrix[3*counter+2][alphabet.index(l[i])] += 1
               i += 1
            counter += 1
         else:
            if(l[i] != "-"):
               print "i is "+ str(i)
               print l[i]
               print (i < (len(l)))
               emissionMatrix[3*counter+1][alphabet.index(l[i])] += 1
   emissionMatrix1 = [[0  for i in range(len(alphabet)) ] for j in range(tmColNum)]
   for i, l in enumerate(emissionMatrix):
      if sum(l) >0:
         for j, s in enumerate(l):
            emissionMatrix1[i][j] = s/sum(l)
   emissionMatrix2 = [[0  for i in range(len(alphabet)) ] for j in range(tmColNum)]
   print "length is sss " + str(len(emissionMatrix1))
   for i, l in enumerate(emissionMatrix1):
      if (i % 3) != 0 :
         for j, s in enumerate(l):
            emissionMatrix2[i][j] = (s + pseudocount)/(sum(l) + pseudocount * len(alphabet))
   emissionMatrix2[len(emissionMatrix2)-1] = [0 for _ in range(len(alphabet))]
   return emissionMatrix2

def main():
    f = open('/Users/tingliu/Downloads/dataset_11632_4 (2).txt', 'r')
    temp = f.readline().split(" ")
    threshold = float(temp[0].strip())
    pseudocount = float(temp[1].strip())
    print threshold
    print pseudocount
    f.readline()
    alphabet = f.readline().strip().split(" ")
    f.readline()
    ml = [list(f.readline().strip()) + ["$"]]
    for l in f:
       # append a $ sign at the end
       temp = list(l.strip()) + ["$"]
       print temp
       ml.append(temp)
    colNum = findWhichColumn2Remove(threshold, ml)
    tm1 = generateTransitionMatrix(threshold, alphabet, ml, colNum)
    pseudocount = 0.01
    tm = addPseudocount2TransitionMatrix(tm1, pseudocount, len(colNum))
    print tm
    fp =  open('/Users/tingliu/Downloads/res5.txt', 'w')
    colNum = findWhichColumn2Remove(threshold, ml)
    colNames = ["S", "I0"]
    for i in range(1, len(colNum)):
       colNames = colNames + ["M"+str(i), "D"+str(i), "I"+str(i)]
    colNames = colNames + ["E"]
    for colName in colNames:
      fp.write("%s\t" % colName)
    fp.write("\n")
    for i in range(len(tm)):
       fp.write("%s\t" % colNames[i])
       for j in range(len(tm[0])):
          fp.write("%s\t" % tm[i][j])
       fp.write("\n")

    fp.write("--------\n")
    em = generateEmissionMatrix(threshold, alphabet, ml, colNum, pseudocount)
    print "em is "
    print(em)
    for a in alphabet:
       fp.write("%s\t" % a)
    fp.write("\n")
    for i in range(len(em)):
       fp.write("%s\t" % colNames[i])
       for j in range(len(em[0])):
           fp.write("%s\t" % em[i][j])
       fp.write("\n")



if __name__ == "__main__":
    main()