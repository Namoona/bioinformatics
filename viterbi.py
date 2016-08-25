from __future__ import division
import math

def viterbiToGetMostProbablePath(string, alphabet, states, transition, emissionProb):
   curProb = [[0 for x in range(len(string))] for y in range(len(states))]
   for i in range(len(states)):
       curProb[i][0] = math.log(float(1/len(states)))

   paths = [[0 for x in range(len(string)-1)] for y in range(len(states))] 
   path = ""
   for i, k in enumerate(string):
      ind1 = alphabet.index(k)
      if i == 0:
          for s in range(len(states)):
             curProb[s][i] = curProb[s][i] + math.log(emissionProb[s][ind1])
             print "curProb is" + str(curProb)
      else:
          print "i is " + str(i)
          for s1 in range(len(states)):
             probs = []
             for s2 in range(len(states)):
                 probs.append(curProb[s2][i-1] + float(math.log(transition[s2][s1])) + float(math.log(emissionProb[s1][ind1])))
             # print probs
             # print i
             # print s1
             # print curProb
             curProb[s1][i] = max(probs)
             paths[s1][i-1] = states[probs.index(max(probs))]
          # prob0 = curProb[0] + float((transition[0][0])) + float((emissionProb[0][ind1]))
          #           prob1 = curProb[1] + float((transition[1][0])) + float((emissionProb[0][ind1]))
          #           prob2 = curProb[0] + float((transition[0][1])) + float((emissionProb[1][ind1]))
          #           prob3 = curProb[1] + float((transition[1][1])) + float((emissionProb[1][ind1]))
          #           print prob0
          #           print prob1
          #           print prob2
          #           print prob3
          #           curProb = [max(prob0, prob1), max(prob2, prob3)]
          #           if prob0 > prob1:
          #               paths[0][i-1] = states[0]
          #           else:
          #               paths[0][i-1] = states[1]
          #           if prob3 > prob2:
          #               paths[1][i-1] = states[1]
          #           else:
          #               paths[1][i-1] = states[0]
   
   # traceback
   print curProb
   
   tmp = []
   for i in range(len(states)):
      tmp.append(curProb[i][len(string)-1])
   path = states[tmp.index(max(tmp))]
   prev = tmp.index(max(tmp))
   for i in reversed(range(1, len(string))):
      path = paths[prev][i-1]+ path
      prev = states.index(paths[prev][i-1])
      print prev
      print path
   return path



   # prev = 0
   #  if curProb[0] > curProb[1]:
   #     path = states[0]
   #     prev = 0
   #  else:
   #     path = states[1]
   #     prev = 1
   #  print paths
   #  print path
   


def main():
    f = open('/Users/tingliu/Downloads/dataset_11594_6 (1).txt', 'r')
    string = f.readline().strip()
    f.readline()
    alphabet = f.readline().strip().split(' ')
    f.readline()
    states = f.readline().strip().split(' ')
    f.readline()
    f.readline()

    transitionProb = []
    for _ in range(len(states)):
        l = f.readline()
        trp2 = l.strip().split('\t')
        trp = trp2[1:]
        trp = [float(x) for x in trp]
        transitionProb.append(trp)

    f.readline()
    f.readline()
    emissionProb = []
    for _ in range(len(states)):
        l = f.readline()
        trp2 = l.strip().split('\t')
        trp = trp2[1:]
        trp = [float(x) for x in trp]
        emissionProb.append(trp)

    path = viterbiToGetMostProbablePath(string, alphabet, states, transitionProb, emissionProb)
    print path

if __name__ == "__main__":
    main()
    
      
