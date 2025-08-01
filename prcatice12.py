def search (data= [],element = None)
    
    flag = False 
    for index in range(len(data)):
        if data[index] == element:
            print(element,'found at index', index)
            flag = True
            break
    if flag = False
        print(element,'not found at index', index)

        
