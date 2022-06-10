n = int(input())

SUM = 0
for i in range(n):
    row = input().split()

    num1, num2 = int(row[i]), int(row[-i-1])
    
    if num1 % 3 == 1:
        SUM += num1 
    if num2 % 3 == 1:
        SUM += num2 

print(SUM)

