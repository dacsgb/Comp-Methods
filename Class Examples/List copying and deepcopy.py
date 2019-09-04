from copy import deepcopy

list1 = [1,2,3,4,5,6,7]
print(list1)

list2 = list1  #a problem here
list1[3]=17
print("list2 changes after change in list 1", list2)

list2[2]=28
print("list1 changes after a change in list 2",list1)

list3 = deepcopy(list1)
list1[4]=25
print("list 3 deepcopy no change after change in list 1",list3)

#creating new lists
new1 = [0]*5
print("\na new list of zeros", new1)
new1[2]=7
print("change only 1 term ", new1)

#creating new matrix ????
nrows, ncols = 6, 4
matrix1 = [[0]*ncols] * nrows
matrix1[2][2]= 494
print("\n",matrix1)  #this doesn't work!!!

#list comprehension (list math) for creating new lists
nrows, ncols = 4, 7
matrix2 = [ [0]* ncols for i in range(nrows)]
matrix2[2][2]= 73
print(matrix2)






