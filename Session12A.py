# Lienar Search
# Time Complexity : O(n)
def search(data=[], element=None):

    flag = False
    for index in range(len(data)):
        if data[index] == element:
            print(element, 'found at index:', index)
            flag = True
            break

    if flag == False:
        print('element', element,'not found')


numbers = [10, 20, 30, 40, 50]
names = ['john', 'jennie', 'anna', 'kim', 'ben']

search(numbers, int(input('Enter a Number: ')))
search(names, 'ben')
search(names, 'sia')