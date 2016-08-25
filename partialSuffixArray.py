def SuffixArray(text, K):
   suffixArray = []
   for i in range(0,len(text)):
         suf = text[(len(text)-i-1):]
         suffixArray.append((suf, (len(text)-i-1)))
   partialSuffixArray = []
   for s, i in enumerate(sorted(suffixArray)):
      if i[1] % K == 0:
       partialSuffixArray.append((s, i[1])) 
   return partialSuffixArray


def main():

   f = open('/Users/tingliu/Downloads/dataset_9809_2 (2).txt', 'r')
   text = f.readline().strip()
   K = int(f.readline().strip())
   res = SuffixArray(text, K)
   fp =  open('/Users/tingliu/Downloads/dataset_9809_2_res.txt', 'w')
   for r in res:
     print str(r)
     fp.write("%d,%d\n" % r)


if __name__ == "__main__":
    main()