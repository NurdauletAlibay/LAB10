...
1) numbers = [1,2,3]
str_numbers = ['One','Two','Three']
roman_numbers = ['I','II','III']
result = zip(numbers, str_numbers, roman_numbers)
print(result)
print(list(result))

ответ:[(1, 'One', 'I'), (2, 'Two', 'II'), (3, 'Three', 'III')]
...

...
2) py_string = 'Python'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3) 
print(py_string[slice_object])  # Pyt

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
print(py_string[slice_object])   # yhn

ответ: Pyt
       yhn
...

...
3) py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices 0, 1 and 2
slice_object = slice(3)
print(py_list[slice_object]) # ['P', 'y', 't']

# contains indices 1 and 3
slice_object = slice(1, 5, 2)
print(py_tuple[slice_object]) # ('y', 'h') 

ответ:['P', 'y', 't']
       ('y', 'h')
...


...
4) #CALCULATOR
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
        ...

...
5) from decimal import Decimal

# normal float
num = 2.675
print(round(num, 2))

# using decimal.Decimal (passed float as string for precision)
num = Decimal('2.675')
print(round(num, 2))

ответ: 2,67
       2,68

...

...
6)class Polygon:
  def __init__(polygonType):
    print('Polygon is a ', polygonType)

class Triangle(Polygon):
  def __init__(self):

    Polygon.__init__('triangle')
    
print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))

ответ: True
       False
       True
       True
...

...
<<<<<<< HEAD
7)
=======
5) class RomanNumeral:

    """Римская цифра, представленная как строка и число."""

    SYMBOLS = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    def __init__(self, number):
        self.value = number

    @classmethod
    def from_string(cls, string):
        return cls(cls.roman_to_int(string))

    @staticmethod
    def roman_to_int(numeral):
        total = 0
        for symbol, next_symbol in zip_longest(numeral, numeral[1:]):
            value = RomanNumeral.SYMBOLS[symbol]
            next_value = RomanNumeral.SYMBOLS.get(next_symbol, 0)
            if value < next_value:
                value = -value
            total += value
        return total
        ...

        Красотка из Ожета

