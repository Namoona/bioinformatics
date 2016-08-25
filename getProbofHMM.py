import math
def getProb(path, states, transition):
   totalProb = float(math.log(0.5))
   for i, k in enumerate(path):
      if i > 0:
          ind2 = states.index(k)
          ind1 = states.index(path[i-1])
          totalProb = totalProb + float(math.log(transition[ind1][ind2]))
      else:
          totalProb = totalProb + 0
   return totalProb

def main():
    f = open('/Users/tingliu/Downloads/dataset_11594_2.txt', 'r')
    path = f.readline().strip()
    f.readline()
    states = f.readline().strip().split(' ')
    f.readline()
    f.readline()
    transitionProb = []
    for l in f:
        trp2 = l.strip().split('\t')
        trp = trp2[1:]
        trp = [float(x) for x in trp]
        transitionProb.append(trp)
    print transitionProb    
    prob = getProb(path, states, transitionProb)
    print math.exp(prob)

if __name__ == "__main__":
    main()
    
      
   