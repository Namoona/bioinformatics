def SuffixArray(text):
   suffixdict = {}
   for i in range(0,len(text)):
      suf = text[(len(text)-i-1):]
      suffixdict[suf] = (len(text)-i-1)
   return suffixdict

def main():
   patterns = []
   f = open('/Users/tingliu/Downloads/dataset_310_2.txt', 'r')
   text = f.readline().strip()
   suffixDict = SuffixArray(text)
   print(sorted(suffixDict))
   output = []
   for key in sorted(suffixDict):
      print(suffixDict[key])
      output.append(suffixDict[key])
   print(output)
if __name__ == "__main__":
    main()