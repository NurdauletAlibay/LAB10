6) prime_numbers = [2, 3, 5, 7]

   # преобразовать список в bytearray
   byte_array = bytearray(prime_numbers)
   print(byte_array)

7) # Perimeter of Square
def calculatePerimeter(l):
    return 4*l

# Area of Square
def calculateArea(l):
    return l*l

expression = input("Type a function: ")

for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print("If length is ", l, ", Perimeter = ", eval(expression))
    elif (expression == 'calculateArea(l)'):
        print("If length is ", l, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break

8) py_list = ['P', 'y', 't', 'h', 'o', 'n']
   py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

   # содержит индексы 0, 1 и 2
   slice_object = slice(3)
   print(py_list[slice_object]) # ['P', 'y', 't']

   # содержит индексы 1 и 3
   slice_object = slice(1, 5, 2)
   print(py_tuple[slice_object]) # ('y', 'h')

9) # string representation of Luke
   name = str('Luke')
   print(name)

   # string representation of an integer 40
   age = str(40)
   print(age)

   # string representation of a numeric string 7ft
   height = str('7ft')
   print(height) 

10) from decimal import Decimal

    # normal float
    num = 2.675
    print(round(num, 2))

    # используя decimal.Decimal (передается с плавающей запятой в виде строки для точности)
    num = Decimal('2.675')
    print(round(num, 2))

11) class Polygon:
  def __init__(polygonType):
    print('Polygon is a ', polygonType)

class Triangle(Polygon):
  def __init__(self):

    Polygon.__init__('triangle')
    
print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))