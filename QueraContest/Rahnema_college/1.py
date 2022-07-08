n = int(input())
temps = [int(temp) for temp in input().split()]
for temp in temps:
    if temp > 15:
        print("cooler")
    else:
        print("heater")
