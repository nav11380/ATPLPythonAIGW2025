file = open("quotes.txt",'a')
print('keep entering quotes.type to braek')
quote = input('enter a quote:')

while quote != 'quit':
    file.write(quote)
    file.write('\n')
    quote = input('enter quote uh want')

    