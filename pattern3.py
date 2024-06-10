n=int(input())
for i in range(0,5):
  for j in range(0,5):
    if i+j>=n-1:
      print("*",end=' ')
    else:
      print( ' ' ,end='')
  print()