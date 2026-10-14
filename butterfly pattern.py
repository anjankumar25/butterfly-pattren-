"""for i in range(1,6):
    for j in range(i):
        print(i,end="")
    for l in range(i,6):
        print(" ",end="")
    for k in range(i,6):
        print(" ",end="")
    for m in range(i):
            print(i,end="")
    print()
for g in range(1,6):
     for i in range(g,6):
          print(g,end="")
     for m in range(i):
          print("",end="")
     for v in range(g,6):
          print(" ",end="")
     for i in range(g,6):
          print(g,end="") 
    
     print()"""
n=5
for i in range(1,n+1):
    print("*"*i+" "*(2*5-2*i)+"*"*i) 
for j in range(n,0,-1):
    print("*"*j+" "*(2*5-2*j)+"*"*j)

        