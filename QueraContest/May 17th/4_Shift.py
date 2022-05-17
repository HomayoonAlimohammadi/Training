string = input()

if string == ''.join(sorted(string)):
    print(string)

else:
    smallest = string[:]
    for i in range(len(string)):
        string = string[1:] + string[0]
        if string < smallest:
            smallest = string[:]

    print(smallest)