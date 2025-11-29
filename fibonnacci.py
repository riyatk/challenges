limit = int(input("Enter the series limit: "))

a = 0
b = 1

print(a)
print(b)

for i in range(limit - 2):
    c = a + b
    print(c)
    a = b
    b = c
