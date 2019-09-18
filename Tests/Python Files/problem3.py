def WhereIsIt(short1, long1):

    # Iterate through all possible combinations of lengths and starting positions 
    n = len(long1)
    for i in range(n+1):
        for j in range(i,n+1):
            # Compare the lists given to see if one is a subset of another
            if long1[i:j] == short1:
                # return index
                return i
    # If not found, return -1
    return -1

def main():
    a = [8,2,9,2]
    b = [3,5,8,2,9,2,3,4,2,1]
    c = [5,2,1]
    d = [3,6,2,-4,5,2,1]

    print(WhereIsIt(a,b))
    print(WhereIsIt(c,d))
    print(WhereIsIt(c,b))

main()