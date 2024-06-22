n = 19

total = 0
happy = True

      
def check_happy(n):
    
    n = str(n) 
    for i in n:
        i = int(i)
        total += i*i
    return total


while total != 1:
    check_happy(total)
print(total)