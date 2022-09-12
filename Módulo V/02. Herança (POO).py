from email.headerregistry import HeaderRegistry


class Humano:
    def __init__(self, name, weapon, color_eyes):
        self.name = name
        self.weapon = weapon
        self.color_eyes = color_eyes

def get_name(self):
    return f'O nome dele é: {self.name}'

def get_weapon(self):
    return f'A arma utilizada por ele é: {self.weapon}'

def get_color_eyes(self):
    return f'A cor de seus olhos é: {self.color_eyes}'

class Aragorn(Humano):
    def __init__(self, name, weapon, color_eyes, family_member):
        self.family_member = family_member

        super().__init__(name, weapon, color_eyes, family_member) ##instanciando a classe anterior - Humano

    def get_family_member(self):
        if self.family_member == 'Y':
            return f'Esse humano é um herdeiro legitimo de Isildur'

        if self.family_member == 'N':
            return f'Esse humanao é uma mera ralé'

aragorn = Aragorn ('Aragorn II', 'Espada Anduril', 'Cinzentos', 'Isuldur', 'Y')
print (aragorn.get_family_member())