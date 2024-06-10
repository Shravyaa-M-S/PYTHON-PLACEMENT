n=int(input())
for i in range(n):
  for j in range(n):
    if i-j>=n:
      print("*",end=' ')
    else:
      print(" ",end=' ')
  print()
  