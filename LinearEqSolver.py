
def convertInt(arr):
    for x in range(len(arr)):
        if arr[x] == "x" or arr[x] == "+" or arr[x] == "y" or arr[x] == "=":
            pass
        else:
            arr[x] = int(arr[x])
    return arr

def joinNum(array):
    arr = array
    index = 0
    while index < len(arr):
        if arr[index] == " ":
            arr.pop(index)
            index += 0
        index += 1
    #print(arr)
    encVar = False #Encountered Variable
    i = 0
    while i < (len(arr) - 1):
        if arr[i+1] == "x" or arr[i+1] == "+" or arr[i+1] == "-" or arr[i+1] == "y" or arr[i+1] == "=" or arr[i] == "x" or arr[i] == "+" or arr[i] == "-" or arr[i] == "y" or arr[i] == "=":
            encVar = True
            i += 1
        else: encVar = False
        if encVar == False:
            arr[i] += arr[i+1]
            arr.pop((i+1))
            i += 2
    if arr[0] == "x":
        arr.insert(0, "1")
    if arr[0] != "-" and arr[0] != "+":
        arr.insert(0, "+")
    for i in range(len(arr)):
        if arr[i] == "y":
            if arr[i-1] == "-" or arr[i-1] == "+":
                arr.insert(i, "1")
        
    for i in range(len(arr)):
        if arr[i] == "=":
            for j in range(i+2, len(arr)):
                arr[i+1] += arr[j]
            break
    for i in range(len(arr)):
        if arr[i] == "=" and arr[i+1] != "-" and arr[i+1] != "+" and int(arr[i+1]) > 0:
            arr.insert(i+1, "+")
            break
    # now the list is in the form ['+', '21', 'x', '-', '11', 'y', '=', '+', '32']
    arr[0] += arr[1]
    arr.pop(1)
    arr[2] += arr[3]
    arr.pop(3)
    arr[5] += arr[6]
    arr.pop(6)
    return arr

def checkConsistency(a1, a2, b1, b2, c1, c2):
    a = a1 / a2
    b = b1 / b2
    c = c1 / c2
    if a == b and b == c:
        print("This equation has Infinite Solutions.")
        return -1
    elif a == b and b != c:
        print("This equation has No Solution.")
        return 0
    elif a != b:
        return 1
    return -2


def solve(eq1, eq2):
    e1 = list(eq1)
    e2 = list(eq2)
    
    q1 = joinNum(e1)
    q2 = joinNum(e2)
    
    real1 = convertInt(e1)
    real2 = convertInt(e2)
    
    a1, a2 = real1[0], real2[0]
    b1, b2 = real1[2], real2[2]
    c1, c2 = real1[5], real2[5]
    
    check = checkConsistency(a1, a2, b1, b2, c1, c2)
    
    if check == 1 or check == -1:
        if check == -1:
            #print("One solution is,")
            print("Am too lazy to refactor for solving eqs with infinite solutions resulting in ZeroDivisionError")
            
        x = (( b1 * -(c2) ) - ( b2 * -(c1) )) / (( a1 * b2 ) - ( a2 * b1 ))
        y = (( -(c1) * a2 ) - ( -(c2) * a1 )) / (( a1 * b2 ) - ( a2 * b1 ))

        print("x:", x)
        print("y:", y)   
    
    elif check == -2:
        print("Encountering unknown error")


print("Type the pair of linear equations in the format of ax+by=c")
eq1 = input()
eq2 = input()
print()
print("-" * 80, end="")
solve(eq1, eq2)
print("-" * 80)


while True:
    print()
    print("Press enter to quit")
    a = input()
    quit()




