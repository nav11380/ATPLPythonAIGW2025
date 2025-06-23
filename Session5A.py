num1 = -13
num2 = 2
result = num1 >> num2
print('result:', result)

print(bin(num1))        # 1 0 1 1
print(bin(num2))        # 0 0 1 0

"""
    11: 0 0 0 0  1 0 1 1
    11 >> 2
        _ _ 0 0  0 0 1 0
        0 0 0 0  0 0 1 0   => 2


    -11
     11 0 0 0 0  1 0 1 1
        1 1 1 1  0 1 0 0    1's complement 
                       1    2's complement
    -11 1 1 1 1  0 1 0 1 >> 2
        _ _ 1 1  1 1 0 1
        1 1 1 1  1 1 0 1

        do the same process again -> take 2's complement
        0 0 0 0  0 0 1 0
                       1
        0 0 0 0  0 0 1 1 -> -3

    13: 0 0 0 0  1 1 0 1
        1 1 1 1  0 0 1 0
                       1
        1 1 1 1  0 0 1 1
        >> 2
        _ _ 1 1  1 1 0 0
        1 1 1 1  1 1 0 0
                 
        0 0 0 0  0 0 1 1
                       1
        0 0 0 0  0 1 0 0
                  ->  -4
            


"""