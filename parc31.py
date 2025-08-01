numbers = [10,20,30,40,50]
square_numbers = [number**2 for number in numbers]
print('sqaure_number:',square_numbers)

my_numbers = ['Even' if number%2 == 0 else 'odd' for number in numbers]
print(my_numbers)

list1 = [1,2,3]
list2 = [4,5]

result = [
    *[n**2 for n in list1],
    *[n**2 for n in list2],
]

print('result with * opreator:',result)