class SociedadeDoAnel:
    def __init__ (self, name):
        self.name = name    

    def __free_deads(self):   #metodo privado
        return f'Você libertou o Exercito de Mortos'

    def freeing_dead(self,integrante):
        if integrante == 'Aragorn':
            return self.__free_deads()
        return f'Você não é capaz de libertar os mortos'

integrante = SociedadeDoAnel(['Frodo','Boromir','Gandalf','Sam', 'Aragorn', 'Lagolas' 'Pippin','Merry'])

access = integrante.freeing_dead('Frodo')
print (access)

access = integrante.freeing_dead('Aragorn')
print (access)