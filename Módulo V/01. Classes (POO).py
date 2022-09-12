from unicodedata import name


class SociedadeDoAnel:
    def __init__(self, name, type, weapon, particularity):
        self.name = name
        self.type = type
        self.weapon = weapon
        self.particularity = particularity

    def description(self):
        return f'Um dos integrantes da Sociedade do Anel é o {self.name}, ele é um {self.type}, se defende sempre com um(a) {self.weapon} e tem o dever de {self.particularity}'

    def __ring_of_power(self):
        if name == 'Frodo':
            return f'Somente ele pode carregar o anel do poder'


integrante1 = SociedadeDoAnel('Gandalf', 'mago','cajado','Cinzento').description() 
integrante2 = SociedadeDoAnel('Frodo','hobbit', 'Espada Sting','Carregar o Anel').description() 
integrante3 = SociedadeDoAnel('Sam','hobbit','Amizade', 'Auxiliar o Frodo a levar o Anel do Poder, pois ele é burro').description()    
integrante4 = SociedadeDoAnel('Pippin','hobbit','Coragem','Sempre estragar tudo por causa de comida').description() 
integrante5 = SociedadeDoAnel('Mary', 'hobbit', '--', 'Estragar tudo junto com o Pippin').description() 
integrante6 = SociedadeDoAnel('Aragorn', 'humano','Espada Anduril','Ajudar o Frodo a chegar no Mordor').description() 
integrante7 = SociedadeDoAnel ('Boromir','humano', 'espada','Ser invejoso e morrer por ser invejoso').description() 
integrante8 = SociedadeDoAnel ('Legolas','elfo','arco e flecha','Lutar bem e fazer acrobacias desnecessárias').description()  
integrante9 = SociedadeDoAnel ('Gemli','anão','machado','--').description()          

print(integrante7)

# #METODO PRIVADO
#     def search_ring_of_power (self, name):
#         if name == 'Frodo':
#             return self.__ring_of_power()
#DANDO ERRO - PERGUNTAR A THAIS


