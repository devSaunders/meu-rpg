import random

class Personagem: 
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.vida_max = vida
        self.defendendo = False
    
    def esta_vivo(self):
        return self.vida > 0 
    
    def receber_dano(self, dano):
        if self.defendendo:
            dano = dano - 4
            self.defendendo = False
        if dano < 0:
            dano = 0
        self.vida = self.vida - dano
        if self.vida < 0:
            self.vida = 0
    
    def calcular_dano_base(self):
        dano_min = self.ataque - 2
        dano_max = self.ataque + 2
        dano_base = random.randint(dano_min, dano_max)
        return dano_base

    def atacar(self, alvo):
        #calculo quanto de dano vai dar
        dano = self.calcular_dano_base()
        alvo.receber_dano(dano)
        return dano, False
    
    def curar(self):
        cura_min = 8
        cura_max = 15
        cura = random.randint(cura_min, cura_max)
        antes = self.vida
        self.vida += cura
        if self.vida > self.vida_max:
            self.vida = self.vida_max
        cura_real = self.vida - antes
        return cura_real
    
    def defender(self):
        self.defendendo = True

    def status(self):
        return f"Nome: {self.nome} - HP: {self.vida}"  

class Heroi(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
        self.cooldown = 0
    def ataque_especial(self, alvo):
        if self.cooldown > 0:
            return 0, False
        else:
            bonus = 8
            dano = self.calcular_dano_base() + bonus
            alvo.receber_dano(dano)
            self.cooldown = 3
            return dano, True

    def atacar(self, alvo):
        dano = self.calcular_dano_base()
        dano_critico = False
        if random.randint(1, 100) <= 10:
            dano *= 2
            dano_critico = True
        alvo.receber_dano(dano)   
        return dano, dano_critico

class Monstro(Personagem):
    def atacar(self,alvo): #aqui eu tiro o critico do monstro 
        dano = self.calcular_dano_base()
        alvo.receber_dano(dano)
        return dano, False
    
class Orc(Monstro):
    def atacar(self, alvo):
        dano = self.calcular_dano_base()
        if random.randint(1, 100) <=20:
            dano = dano + 3
        alvo.receber_dano(dano)
        return dano, False