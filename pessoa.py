from datetime import datetime
class pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def  __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self. idade = idade
        self.comendo = comendo
        self.falando = falando

    
    def falar(self, assunto):
        if self.comendo:# Se comendo for verdadeiro
            print(f'{self.nome} não pode falar comendo')
            return
        
        if self.falando:# se repetir mais de uma vez ele falando
            print(f'{self.nome} já está falando')
            return


        print(f'{self.nome} está falando {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:# serve para que não repita mais de uma vez
            print(f'{self.nome} não está falando')
            return
        
        print(f'{self.nome} parou de falar')
        self.falando = False
    
    def comer(self, alimento):
        if self.comendo:# serve para não repetir mais de uma vez
            print(f'{self.nome} já está comendo')
            return
        
        if self.falando: # se falando fro verdadeiro
            print(f'{self.nome} não pode comer falando')
            return
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    
    
    def parar_comer(self):
        if not self.comendo:# Se ele não estiver comendo
            print(f'{self.nome} não está comendo')
            return
        
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade