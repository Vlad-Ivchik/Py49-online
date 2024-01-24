class Person:
    country = "Belarus"

    def __init__(self, first_name, last_name, is_married=False):
        self._first_name = first_name
        self._last_name = last_name
        self.__is_married = is_married
        self._last_login = None

    def _say_hello(self):
        return f"Hello, my name is {self._first_name} {self.__is_married}"
    
    def blablabla(self):
        return self._first_name.capitalize()
    
    def set_first_name(self, name):
        if not isinstance(name, str):
            raise ValueError
        self._first_name = name

    def __del__(self):
        pass

    def del_first_name(self):
        print("DELETE FIRST NAME")
        self._first_name = None

    name = property(fdel=del_first_name)

    @property
    def first_name(self):
        import random

        return self._first_name.capitalize() + f"{random.randint(1, 100)}"
    
    @first_name.setter
    def first_name(self, name):
        if not isinstance(name, str):
            raise ValueError
        self._first_name = name

    @first_name.deleter
    def first_name(self):
        self._first_name = None

from abc import ABC, abstractmethod


class Figure:
    def __init__(self, *args, **kwargs):
        print("FIGURE")
        super().__init__(*args, **kwargs)

    def perimeter(self):
        pass

    def square(self):
        pass

    def name(self):
        return self.__class__.__name__


class Circle(Figure):
    pi = 3.14

    def __init__(self, *args, **kwargs):
        print('CIRCL')
        super().__init__(*args, **kwargs)

    def perimeter(self):
        return 2 * self.pi * self.radius
    
    def square(self):
        return self.pi * self.radius ** 2

class A(Figure):
    pass

class Rectangle(A, Figure):
    def __init__(self, *args, **kwargs):
        print('REC')
        super().__init__(*args, **kwargs)


class Kvadrat(Rectangle, Circle):
    def __init__(self, *args, **kwargs):
        print('KV')
        super().__init__(*args, **kwargs)
    def perimeter(self):
        return self._x * 4

def get_perimeter(fig):
    if not isinstance(fig, Figure):
        raise TypeError("Need Figure")
    return fig.perimeter()




class SuperStr(str):
    def is_palindrome(self):
        if self.lower() == self[::-1].lower():
            print("Палиндром")
        else:
            print("Не палиндром")



def finder(string):
    words = string.lower().split()
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    print("Количество повторений: ", max(counter.values()))

    return max(counter, key=counter.get)


class Pizza:
    def __init__(self, *args):
        self.ingridients = args

    @classmethod
    def margaritha(cls):
        return cls("tomato", "cheese")
    
    @staticmethod
    def square(radius):
        return 3.14 * radius ** 2

class ThinPizza(Pizza):
    pass


class Language(ABC):
    @abstractmethod
    def hello(self):
        pass
        
class English(Language):
    def hello(self):
        return "Hello"

class French(Language):
    def hello(self):
        return "Bonjour"

class Russian:
    def hello(self):
        return "Privet"

def say_hello(language: Language) -> str:
    if not isinstance(language, Language):
        raise TypeError("Wrong Language")
    return language.hello()


class Complex:
    def __init__(self, i=0, j=0):
        self.i = i
        self.j = j

    def __add__(self, value) -> "Complex":
        print(self)
        print(value)
        if isinstance(value, Complex):
            return Complex(self.i + value.i, self.j + value.j)
        return Complex(self.i + value, self.j)
    
    def __radd__(self, value) -> int:
        print(self)
        print(value)
        return self.i + value
    
    def __eq__(self, value: "Complex") -> bool:
        return self.i == value.i and self.j == value.j
    
    def __lt__(self, value: "Complex") -> bool:
        return self.i < value.i and self.j < value.j
    
    def __sub__(self, other: "Complex") -> "Complex":
        return Complex(self.i - other.i, self.j - other.j)
    
    def __str__(self):
        return f"{self.i}i + {self.j}j"
    
    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    eng = English()
    fr = French()
    ru = Russian()
    print(say_hello(eng))
    print(say_hello(fr))
    print(say_hello(ru))


class Container:
    def __init__(self, *args):
        self.items = list(args)

    def __getitem__(self, i):
        return self.items[i]
    
    def __len__(self):
        return len(self.items)


def cachable(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            result = func(*args)
            cache[args] = result
        else:
            result = cache[args]
        return result
    return wrapper



class Cache:
    def __init__(self, max_size=50):
        self.cache = {}
        self.max_size = max_size

    def __call__(self, func):
        def wrapper(*args):
            if args not in self.cache:
                result = func(*args)
                if len(self.cache) < self.max_size:
                    self.cache[args] = result
            else:
                result = self.cache[args]
            return result
        return wrapper


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __call__(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter


circle = Circle(2)
circle()

cache1 = Cache(max_size=100)
cache2 = Cache(max_size=200)

@cache1
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

@cache1
def fibonacci2(n):
    pass


def init_a(self, a):
    self.a = a

A = type("A", tuple(), {"aaa": "A", "__init__": init_a})

class A():
    aaa = "A"
    def __init__(self, a):
        self.a = a


class MyMeta(type):
    ...


class MyClass(metaclass=MyMeta):
    ...

class A:
    def __new__(cls):
        ...

    def __init__(self):
        ...

    def __call__(self):
        ...

a = A()
# type()()




class MyException(Exception):
    pass


try:
    raise MyException
except MyException:
    print("IT IS MY EXCEPTION")
