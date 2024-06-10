#strong number
num=int(input())
sum=0
temp=num
while(num):
  f=1
  i=1
  r=num%10
  while(i<=r):
    f=f*i
    i=i+1
  sum=sum+f
  num=num//10
if(temp==sum):
  print("number is strong number")
else:
  print("number is not")