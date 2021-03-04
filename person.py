class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self, other_person):
        return f'Hola {other_person.name} me llamo {self.name}'
    
    def have(self):
        return f'I have {self.age} years'
    
if __name__ == '__main__':
    yet = Person('yet', 20)
    Kevin = Person('Mauricio', 23)

    print(Kevin.greet(yet))
    print(Kevin.have())