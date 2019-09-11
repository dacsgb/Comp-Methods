# Fall 2018 Part 1 Problem 3

def LookingForSum(thisarray, sumval):

    n = len(thisarray)
    for i in range(n+1):
        for j in range(i,n+1):
            if sum(thisarray[i:j]) == sumval:
                return i
    return -1

def main():
    thatarray = [3, 4, 2, -7, 5, 2, 1, -1]

    val1 = LookingForSum(thatarray, -2)
    print("val1 = ", val1)     
    
    val2 = LookingForSum(thatarray, 8)
    print("val2 = ", val2)

main()