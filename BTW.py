def BWTmatrix(text):
   allBWT = [text]
   for i in range(1,len(text)):
      allBWT.append(text[i:] +text[0:i])
   print allBWT
   return allBWT

def BWT(text):
    toStore = ""
    BWTmat = BWTmatrix(text)
    for t in sorted(BWTmat):
        toStore = toStore +t[-1]
    return toStore



def main():
   text = "ACCAACACTG$"
   t = BWT(text)
   print t


if __name__ == "__main__":
    main()