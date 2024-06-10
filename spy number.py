#spy number
num=int(input("enter the number to check : "))
sum=0
temp=num
product=1
while(num>0):
  digit=num%10
  sum=sum+digit
  product=product*digit
  num=num//10
if(sum==product):
  print(temp , " is a spy")
else:
  print( temp ," is not")