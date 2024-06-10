#Neon
sum=0
num=int(input("enter the number to check : "))
temp=num
product=1

square=num*num
while(square!=0):
  digit=square%10
  sum=sum+digit
  square=square//10
if(num==sum):
  print((str(num )) +  " is a neon")
else:
  print((str(num )) +  " is not")