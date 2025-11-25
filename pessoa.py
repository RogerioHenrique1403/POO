from datetime import datetime


class pessoa:
    ano_atual = int(datetime.strftime(
        datetime.now(), '%Y'))  # atributo de classe

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self. idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:  # Se comendo for verdadeiro
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:  # se repetir mais de uma vez ele falando
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} está falando {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:  # serve para que não repita mais de uma vez
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:  # serve para não repetir mais de uma vez
            print(f'{self.nome} já está comendo')
            return

        if self.falando:  # se falando fro verdadeiro
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:  # Se ele não estiver comendo
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
        # return self.ano_atual - self.idade

    @classmethod
    # se eu quiser criar uma pessoa por ano de nascimento. E esse metodo que vamos usar será metodo de classe o metodo que usamos anteriormente metodo de instância
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


# testando metodo de classe
p1 = pessoa.por_ano_nascimento('Luiz', 1987)
print(p1.idade)
p1.get_ano_nascimento()
