amounts = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
n = int(input())
for i in range(n):
    num = int(input()) - 1
    amounts[num] = 0

amount = int(input())
if amount > sum(amounts)/(10-n):
    print("deal")
else:
    print("no deal")

