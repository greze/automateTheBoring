def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1
    
        

print("Choose an interger")
try:
    interger = int(input())


except NameError:
    print('Enter an interger')
    interger = int(input())
    
while interger != 1:
    print(collatz(interger))
    interger = collatz(interger)