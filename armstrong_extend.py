num = int(input("Enter the range: "))

for i in range(1,num):
    armstrong = 0
    original = i
    digits = len(str(i))
    flag = True
    
    while i > 0:
                
        last = i % 10        
        armstrong = armstrong + last **digits
        i = i // 10

    if  original == armstrong:
        print(armstrong)
    


