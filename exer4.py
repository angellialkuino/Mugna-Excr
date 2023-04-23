

stringinp = input("Enter string: ").lower()

stringinp = ''.join(ch for ch in stringinp if ch.isalnum() or ch.isspace()).split()

count = {x: stringinp.count(x) for x in set(stringinp) }

print(count)

