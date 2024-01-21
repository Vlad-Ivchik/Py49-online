class Soda:
    def __init__(self, taste=None):
        if isinstance(taste, str):
            self.taste = taste
        else:
            self.taste = None

    def taster(self):
        if self.taste:
            print(f'У вас газировка с {self.taste} вкусом')
        else:
            print('У вас обычная газировка')


cola = Soda('клубничным')

cola.taster()
