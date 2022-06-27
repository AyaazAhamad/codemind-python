num=input()
l=len(num)
num=int(num)
temp=num
sum=0
while(num!=0):
  rem=num%10
  sum=sum+pow(rem,l)
  num=num//10
  l=l-1
if temp==sum:
    print(True)
else:
    print(False)