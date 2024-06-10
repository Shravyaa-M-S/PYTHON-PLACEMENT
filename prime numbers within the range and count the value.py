start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
count = 0

for i in range(start, end + 1):
    if i > 1:  # Prime numbers are greater than 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)
            count += 1

print("Total prime numbers are:", count)
