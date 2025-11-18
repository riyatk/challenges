num = int(input("Enter a number: "))
number = num
armstrong = 0
length = len(str(num))

while number > 0 :

    last = number % 10
    armstrong = armstrong + last **length
    number = number // 10

if num == armstrong:
    print(num," is an armstrong number!")
else:
    print(num," is not an armstrong number!")