import math
def getProbOutcomeGivenHidden(string, alphabet, path, states, emissionProb):
   totalProb = 0
   for i, k in enumerate(path):
          ind1 = states.index(k)
          ind2 = alphabet.index(string[i])
          totalProb = totalProb + float(math.log(emissionProb[ind1][ind2]))
   return totalProb

def main():
    f = open('/Users/tingliu/Downloads/dataset_11594_4.txt', 'r')
    string = f.readline().strip()
    f.readline()
    alphabet = f.readline().strip().split(' ')
    f.readline()
    path = f.readline().strip()
    f.readline()
    states = f.readline().strip().split(' ')
    print states
    emissionProb = []
    f.readline()
    f.readline()
    for l in f:
        trp2 = l.strip().split('\t')
        trp = trp2[1:]
        trp = [float(x) for x in trp]
        emissionProb.append(trp)
    print emissionProb    
    prob = getProbOutcomeGivenHidden(string, alphabet, path, states, emissionProb)
    print math.exp(prob)

if __name__ == "__main__":
    main()
    
      
