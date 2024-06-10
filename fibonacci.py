def fibonacci(n):
  x,y=0,1
  for i in range(2,n):
    print(x)
    x,y=y,x+y
x=int(input())
fibonacci(x)
