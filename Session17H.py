from Session17G import Visitor

vistor = Visitor()
vistor.add_visitor()
print(vistor.to_csv())

file = open('visitors.csv', 'a')
file.write(vistor.to_csv())