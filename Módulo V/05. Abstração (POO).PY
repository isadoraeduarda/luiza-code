from email import message
from time import time


import time 

class Gandalf:

    def __init__(self, grey, white):
        self.grey = grey
        self.white = white

    def turning_white(self):
        start = time.time()
    
        mensagem = f'Para o Mago {self.grey}, a Mago {self.white}, '
        mensagem += f'Morreu em Mountin of Doom {time.time()} (Sociedade do Anel)'
        time.sleep(10)

        mensagem += f'Voltou sendo salvo por Eru para derrotar o Saruman (Duas Torres) {time.time}'
        time.sleep(15)

        end = time.time()
        hiato_gandalf = end = start

        return mensagem + f'O tempo do Mago Cinzento para se tornar o Mago branco foi de: {hiato_gandalf}'

gandalf = Gandalf ('Morrer, viver e salvar todos', 'Mago')

gandalf = (gandalf.turning_white())

print(gandalf.turning_white())
