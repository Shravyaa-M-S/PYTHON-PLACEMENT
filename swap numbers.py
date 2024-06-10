def swap_numbers(a,b):
  print("a=" ,a)
  print("b= ",b)
  temp=a
  a=b
  b=temp
  print("a= ",a)
  print("b= ",b)
  return a,b
num1=int(input( ))
num2=int(input( ))
num1,num2=swap_numbers(num1,num2)
