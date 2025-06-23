white_square = '\u25A0'
black_square = '\u25A1'

# print(white_square)
# print(black_square)

for row in range(0, 9):
    if row % 2 == 0:
        print(white_square, end=' ')
    else:
        print(black_square, end=' ')

print()

for row in range(0, 9):
    if row % 2 == 0:
        print(black_square, end=' ')
    else:
        print(white_square, end=' ')

print()
