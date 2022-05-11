s = '123'
print(str(filter(lambda char: char.isalpha() or char.isdigit(), s)))