"""
    Sorting Algorithm
    Bubble Sort

    Initial Cycle                1
    10, 30, 50, 20, 40

    10, 30
    10, 30, 50, 20, 40

    30, 50
    10, 30, 50, 20, 40

    50, 20
    10, 30, 20, 50, 40

    50, 40
    10, 30, 20, 40, 50

    
    Next Cycle                      2
    10, 30, 20, 40, 50 (s)

    10, 30
    10, 30, 20, 40, 50 (s)

    30,20
    10, 20, 30, 40, 50 (s)

    30,40
    10, 20, 30, 40, 50 (s)

    10, 20, 30, 40 (s), 50 (s)

    Next Cycle                           3
    10, 20, 30, 40 (s), 50 (s)

    10,20
    10, 20, 30, 40 (s), 50 (s)

    20,30
    10, 20, 30 (s), 40 (s), 50 (s)

    Next Cycle                          4
    10, 20, 30 (s), 40 (s), 50 (s)

    10,20
    10(s), 20(s), 30 (s), 40 (s), 50 (s)


"""

a = 10
b = 20

temp = a
a = b
b = temp

print('a:',a)
print('b:',b)


#           0  1
# numbers = [10, 5]

#.          0.  1.  2.  3.  4. 
numbers = [10, 30, 50, 20, 40]

# outer: 0, 1, 2, 3
for outer in range(len(numbers)-1):

    for inner in range(len(numbers)-outer-1):
    
        if numbers[inner] > numbers[inner+1]:
            temp = numbers[inner]
            numbers[inner] = numbers[inner+1]
            numbers[inner+1] = temp


print(numbers)

"""
numbers: [10, 30, 50, 20, 40]

outer  : 0, 1, 2, 3
outer  : 0
numbers: 10, 30, 50, 20, 40
----------
inner  : 5-0-1 -> 4, 0 to 3
inner  : 0, 10 > 30 ?
         10, 30, 50, 20, 40
inner  : 1, 30 > 50 ?
         10, 30, 50, 20, 40
inner  : 2, 50 > 20 ?
         10, 30, 20, 50, 40
inner  : 3, 50 > 40 ?
         10, 30, 20, 40, 50

----------
outer  : 1
numbers: 10, 30, 20, 40, 50


"""
