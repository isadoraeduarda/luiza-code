from typing_extensions import Self


class Fear:
    def __init__(self):
        pass
    
    def form_fear (self):
        return 'Indefinido'

class FearGollom (Fear):
    def __init__(self, fear):
        self.fear = fear
        super().__init__()
    
    def form_fear (self):
        return f'O medo do Gollum é: {self.fear}'

class FearAragorn (Fear):
    def __init__(self, fear):
        self.fear = fear
        super().__init__()
    
    def form_fear (self):
        return f'O medo do Aragorn é: {self.fear}'

fear_gollum = FearGollom ('Ser o Smeagol para sempre')
print (fear_gollum.form_fear())

fear_aragorn = FearAragorn ('Se tornar o pai dele')
print (fear_aragorn.form_fear()) 



#Erro bem diferente"
