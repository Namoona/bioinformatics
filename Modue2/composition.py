import sys # you must import "sys" to read from STDIN
def composition(k, text):
    allComp = []
    for i in range(len(text)-k+1):
        allComp.append(text[i:i+k])
    return allComp


def main():
   f = open('/Users/tingliu/Downloads/dataset_197_3.txt', 'r')
   num = int(f.readline().strip())
   print num
   text = f.readline().strip()
   output = composition(num, text)
   fp =  open('/Users/tingliu/Downloads/res2.txt', 'w')
   for r in sorted(output):
      fp.write("%s\n" % r)

if __name__ == "__main__":
    main()