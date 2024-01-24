class Math:

    @staticmethod
    def addition(x, y):
        print(x + y)

    @staticmethod
    def subtraction(x, y):
        print(x - y)

    @staticmethod
    def multiplication(x, y):
        print(x * y)

    @staticmethod
    def division(x, y):
        print(x / y)

    pass


obj = Math()
obj.addition(3, 3)
obj.subtraction(3, 3)
obj.multiplication(3, 3)
obj.division(3, 3)