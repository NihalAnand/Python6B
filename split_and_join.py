def split_and_join(line):
  
   line=line.split(" ")
   line="-".join(line)
   return line
n=input()
print(split_and_join(n))