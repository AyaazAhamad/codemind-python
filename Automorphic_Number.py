n=int(input())
digits=len(str(n))
s=n**2
last=s%pow(10,digits)
if last==n:
   print("Automorphic Number")
else:
    print("Not an Automorphic Number")