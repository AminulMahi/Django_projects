n = list(input("Enter a lsit: "))
n.reverse()
print(n)
n[::-1]
print(n)

temp = n[0]
n[0] = n[-0]
n[-0] = temp
print(n)