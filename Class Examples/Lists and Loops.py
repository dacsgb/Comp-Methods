def printlist(mylist):
    for val in mylist:
        print(val)
    return

def pl2(alist):
    print("\n",len(alist)," length of alist \n")
    for i in range(len(alist)):
        print(alist[i])
    #next i

def printmat(mymat):
    print("\n\nprinting mymat")
    for row in range(len(mymat)):
        for col in range(len(mymat[row])):
            print(mymat[row][col])

def arraysum(thelist):
    sum=0
    for num in thelist:
        #sum=sum+num
        sum += num
    return sum


def matrixsum(thematrix):
    sum=0
    for rowvals in thematrix:
        for colval in rowvals:
            sum += colval
        #next colval
    #next rowvals
    return sum


def main():
    ralph=[1,3,5,2,4,9,3,5,-2,11.7]
    gerald=[[1,2,3,4],[5,6,7],[5,6,7,8],[5,6,7,8],[4,3,2,1]]
    #note row 1 only has 3 terms
    #printlist(ralph)
    #pl2(ralph)
    #print("\n",ralph)
    #printmat(gerald)
    #a=arraysum(ralph)
    cc=matrixsum(gerald)

    print(cc)


main()





