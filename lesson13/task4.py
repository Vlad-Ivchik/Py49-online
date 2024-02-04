from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Gav"


class Cat(Animal):
    def speak(self):
        return "Murr"


class AnimalFactory:
    def create_animal(self, type_animal):
        if type_animal == "dog":
            return Dog()
        elif type_animal == "cat":
            return Cat()
        else:
            raise ValueError


if __name__ == "__main__":
    factory = AnimalFactory()

    dog = factory.create_animal("dog")
    print(dog.speak())

    cat = factory.create_animal("cat")
    print(cat.speak())
