class Dog:
    '''This defines a dog'''
    def __init__(self, name, breed,color) -> None:
        self.name = name
        self.__breed = breed
        self.__color = color
    
    def bark(self):
        return 'Woof woof'

    def walk(self):
        return f'{self.name} is walking'
    
    def party(self):
        pass

class Cat:
    '''This defines a cat'''
    def __init__(self,name,breed,color):
        self.name = name
        self.__breed = breed
        self.__color = color
    
    def meow(self):
        pass
    
    def walk(self):
        pass

    def play(self,ball):
        pass