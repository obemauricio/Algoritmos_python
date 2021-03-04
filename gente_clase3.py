class Gente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def len_nombres(self, otra_persona):
        if len(self.nombre) > len(otra_persona.nombre):
            f'el nombre de {self.nombre} es mas largo que {otra_persona.nombre}'
        elif len(self.nombre) < len(otra_persona.nombre):
            f'El nombre de {self.nombre} es menor que {otra_persona.nombre}'
        else:
            return f'los nombres de {self.nombre} tiene la misma cantidad de caracteres que {otra_persona.nombre}'

    def mayor_o_menor(self, otra_persona):
        if self.edad > otra_persona.edad:
            return f'{self.nombre} es mayor que {otra_persona.nombre}'
        elif self.edad < otra_persona.edad:
            return f'{self.nombre} es menor que {otra_persona.nombre}'
        else:
            return f'{self.nombre} tiene la misma edad que {otra_persona.nombre}'

if __name__ == '__main__':
    person1 = Gente('Johan', 23)
    person2 = Gente('Mario', 24)
    print(person1.mayor_o_menor(person2))
    print(person1.len_nombres(person2))        