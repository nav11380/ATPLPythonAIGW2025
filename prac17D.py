from prac17C import Visitor

visitor = Visitor()
visitor.add_visitor()
print(visitor.to_csv)

file = open('visitor_csv','a')
file.write(visitor.to_csv)