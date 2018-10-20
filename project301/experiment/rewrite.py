import sys

with file(sys.argv[1],'r') as f:
   fin=f.read()
   print(fin)
   for i in fin:
      i.replace("_",'-')
   print(i)

with file(sys.argv[2],"w") as newfile:
   newfile.write(i)


