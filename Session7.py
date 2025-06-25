# Whenever python program is executed, 
# it is executed by the main thread

# Magic Variables or Dunders
# print('__name__ is:', __name__) # output : __main__

# you can keep the name main or kuchbhi

# main function
def main():
    print('this is first statement')

    for index in range(0,5):
        print(index)

    print('this is last statement')


# We need to manually(explicitly) execute the main function
if __name__ == '__main__':
    main()