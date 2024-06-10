def is_palindrome(n):
    return str(n) == str(n)[::-1]

n = int(input())
if is_palindrome(n):
    print("Yes")
else:
    print("No")
