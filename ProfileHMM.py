from __future__ import division

def findWhichColumn2Remove(threshold, ml):
   colNum = []
   newMultipleAlignment = []
   for i in range(len(ml[0])):
      col = []
      for l in ml:
         col.append(l[i])
      newMultipleAlignment.append(col)
      if col.count("-")/len(ml) < threshold:
         colNum.append(i)
   return (colNum, newMultipleAlignment)

def findAllDelIndices(my_list, cha):
   indices = [i for i, x in enumerate(my_list) if x == cha]
   return indices

def findAllIndices(my_list, cha):
   indices = [i for i, x in enumerate(my_list) if x != cha]
   return indices

def generateTransitionMatrix(threshold, alphabet, ml):
   colNum, newMultipleAlignment = findWhichColumn2Remove(threshold, ml)
   tmColNum = (len(colNum))*3 + 3
   transitionMatrix = [[0  for i in range(tmColNum)] for j in range(tmColNum)]
   currentline = newMultipleAlignment[0]
   if(0 in colNum):
       transitionMatrix[0][2] =(len(currentline) - currentline.count("-")) / len(currentline)
       transitionMatrix[0][3] = currentline.count("-")/len(currentline)
   else:
       transitionMatrix[0][1] = (len(currentline) - currentline.count("-"))/len(currentline)
   for i, cn1 in enumerate(colNum):
    print "i is " + str(i)
    print "cn is " + str(cn1)
    if((i+1) < len(colNum)):
      cn2 = colNum[i+1]
      col1 = newMultipleAlignment[cn1]
      col2 = newMultipleAlignment[cn2]
      match1match = findAllIndices(col1, "-")
      match1deletion = findAllDelIndices(col1, "-")
      diff = cn2 - cn1
      match2match = findAllIndices(col2, "-")
      match2deletion = findAllDelIndices(col2, "-") 
      mm = 0
      md = 0
      dm = 0
      dd = 0
      if diff == 1:
         for j in range(len(col1)):
            if(j in match1match):
                if j in match2match:
                   mm= mm+1
                else:
                   md = md+1
            else:
                if j in match2match:
                   dm = dm + 1
                else:
                   dd = dd+1
         transitionMatrix[(i)*3+2][(i+1)*3+2] = mm / len(match1match)
         transitionMatrix[(i)*3+2][(i+1)*3+3] = md / len(match1match)
         if (len(match1deletion) > 0):
            transitionMatrix[(i)*3+3][(i+1)*3+2] = dm / len(match1deletion)
            transitionMatrix[(i)*3+3][(i+1)*3+3] = dd / len(match1deletion)
      else:
         deletionIndices = []
         for j in range(cn1+1, cn2):
            coln = newMultipleAlignment[j]
            deletionIndices = deletionIndices + findAllDelIndices(coln, "-")
         print range(len(col1))
         print deletionIndices
         for j in range(len(col1)):
            if deletionIndices.count(j) == (diff-1):
               if (j in match1match):
                  if (j in match2match):
                     mm = mm+1
                  else:
                     md = md + 1
               else:
                  if (j in match2match):
                     dm = dm + 1
                  else:
                     dd = dd + 1
         transitionMatrix[(i)*3+2][(i+1)*3+2] = mm / len(match1match)
         transitionMatrix[(i)*3+2][(i+1)*3+3] = md / len(match1match)
         transitionMatrix[(i)*3+2][(i+1)*3+1] = 1- mm / len(match1match) - md/len(match1match) 
         
         if len(match1deletion) > 0:
            transitionMatrix[(i)*3+3][(i+1)*3+1] = dm / len(match1deletion)
            transitionMatrix[(i)*3+3][(i+1)*3+2] = dd / len(match1deletion)
         
         insertNum = len(col1) * (diff-1) - len(deletionIndices)
         insert2match = len(col1) - mm-md-dm-dd - (len(match2deletion) - md - dd)
         insert2del = len(match2deletion) - md - dd
         print insertNum
         print insert2match
         print (i+1)*3+1
         transitionMatrix[(i+1)*3+1][(i+1)*3+3] = insert2del / insertNum
         transitionMatrix[(i+1)*3+1][(i+1)*3+2] = insert2match / insertNum
         transitionMatrix[(i+1)*3+1][(i+1)*3+1] = (insertNum-insert2match - insert2del) / insertNum
      matchSum = 0
      delSum = 0
      insertSum = 0
      print transitionMatrix
      if (colNum[len(colNum)-1] == (len(newMultipleAlignment)-1)):
         for k in range(len(transitionMatrix)):
            matchSum = matchSum + transitionMatrix[k][len(transitionMatrix)-4]
            delSum = delSum + transitionMatrix[k][len(transitionMatrix)-3]
            insertSum = insertSum + transitionMatrix[k][len(transitionMatrix)-2]
         if(matchSum > 0):
            transitionMatrix[len(transitionMatrix)-4][len(transitionMatrix)-1] = 1
         if(delSum > 0):
            transitionMatrix[len(transitionMatrix)-3][len(transitionMatrix)-1] = 1
         if (insertSum > 0):
            transitionMatrix[len(transitionMatrix)-2][len(transitionMatrix)-1] = 1
      else: #lastCol was an insertion
         lastCol = newMultipleAlignment[len(newMultipleAlignment)-1]
         lastmatch = findAllDelIndices(lastCol, "-")
         secondLast = newMultipleAlignment[len(newMultipleAlignment)-2]
         slmatch = findAllIndices(secondLast, "-")
         sldel = findAllDelIndices(secondLast, "-")
         mi = 0
         me = 0
         di = 0
         de = 0
         for j in range(len(lastCol)):
            if j in slmatch:
               if j in lastmatch:
                  me = me + 1
               else:
                  mi = mi + 1
            else:
               if j in lastmatch:
                  de = de + 1
               else:
                  di = di + 1
         transitionMatrix[len(transitionMatrix)-4][len(transitionMatrix)-1] =  me / (me + mi)
         transitionMatrix[len(transitionMatrix)-4][len(transitionMatrix)-2] =  mi / (me + mi)
         if ( de + di > 0):
            transitionMatrix[len(transitionMatrix)-3][len(transitionMatrix)-1] =  de / (de + di)
            transitionMatrix[len(transitionMatrix)-3][len(transitionMatrix)-2] =  di / (de + di)
         transitionMatrix[len(transitionMatrix)-2][len(transitionMatrix)-1] =  1


   return transitionMatrix

def generateEmissionMatrix(threshold, alphabet, ml):
   colNum, newMultipleAlignment = findWhichColumn2Remove(threshold, ml)
   tmColNum = (len(colNum))*3 + 3
   emissionMatrix = [[0  for i in range(len(alphabet)) ] for j in range(tmColNum)]
   print emissionMatrix
   i = 0
   while(i < (len(newMultipleAlignment))-1):
     if (i in colNum):
           counts = []
           totalcounts = 0
           for k in alphabet:
              counts.append(newMultipleAlignment[i].count(k) / len(findAllIndices(newMultipleAlignment[i], "-")))
           print "index is " + str(colNum.index(i))
           emissionMatrix[(colNum.index(i))*3+2] = counts
           i = i + 1
     else:
           i2 = i
           while((i2 not in colNum) and i2 < (len(newMultipleAlignment))):
              i2= i2+ 1
           totalcounts = 0
           counts = [0 for ii in range(len(alphabet))]
           print "i s is " + str(i)
           print "i2 is " + str(i2)
           for j in range(i, i2):
              print "j is " + str(j)
              for l, k in enumerate(alphabet):
                  counts[l] = counts[l] + newMultipleAlignment[j].count(k)
                  totalcounts = totalcounts + newMultipleAlignment[j].count(k)
                  print newMultipleAlignment[j]
                  print "alphabet k is " + k
                  print "count is " + str(counts[l])
                  print alphabet

           for l, k in enumerate(alphabet):
              emissionMatrix[(i)*3+1][l] = counts[l]/totalcounts
           i = i2
   print i
   print len(newMultipleAlignment)-1
   if (i  == len(newMultipleAlignment)-1):
           lastCol = newMultipleAlignment[i]
           counts = [0 for ii in range(len(alphabet))]
           for l, k in enumerate(alphabet):
              counts[l] = lastCol.count(k)/len(findAllIndices(lastCol, "-"))
           print counts
           print i
           print colNum
           if i not in colNum:
              emissionMatrix[tmColNum-2] = counts
           else:
               emissionMatrix[tmColNum-4] = counts
   return emissionMatrix
      
      

def main():
    f = open('/Users/tingliu/Downloads/dataset_11632_2 (3).txt', 'r')
    threshold = float(f.readline().strip())
    f.readline()
    alphabet = f.readline().strip().split("\t")
    f.readline()
    ml = [list(f.readline().strip())]
    for l in f:
       ml.append(list(l.strip()))
    tm = generateTransitionMatrix(threshold, alphabet, ml)
    print tm
    fp =  open('/Users/tingliu/Downloads/res5.txt', 'w')
    colNum, newMultipleAlignment = findWhichColumn2Remove(threshold, ml)
    colNames = ["S", "I0"]
    for i in range(1, len(colNum)+1):
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
    em = generateEmissionMatrix(threshold, alphabet, ml)
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