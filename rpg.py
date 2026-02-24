import random

class Personagem: 
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.vida_max = vida
    def esta_vivo(self):
        return self.vida > 0 
    def receber_dano(self, dano):
        self.vida = self.vida - dano
        if self.vida < 0:
            self.vida = 0
    def atacar(self, alvo):
        #calculo quanto de dano vai dar
        dano_min = self.ataque - 2
        dano_max = self.ataque + 2
        dano_real = random.randint(dano_min, dano_max)
        dano_critico = False
        #aqui eu vejo se vai ser dano critico ou nao
        if random.randint(1, 100) <= 10:
            dano_real *= 2
            dano_critico = True
        alvo.receber_dano(dano_real)
        return dano_real, dano_critico
    
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

    def status(self):
        return f"Nome: {self.nome} - HP: {self.vida}"  

nome = input("informe o nome do seu personagem: ")
print("-" * 25)
p1 = Personagem(nome, 100, 10)
monstro = Personagem("goblin", 80, 8)

while p1.esta_vivo() and monstro.esta_vivo(): #este while é a batalha do goblin contra o seu personagem 
    print(p1.status())
    print(monstro.status())
    menu = input("""O que voce deseja fazer agora? 
    1. atacar 
    2. Curar """)
    print("-" * 25)
    
    while menu != "1" and menu != "2": 
        print("Opcao invalida!")
        menu = input("O que voce deseja fazer? ")
        print("-" * 25)

    if menu == "1":
        #Heroi dando dano no Monstro
        dano_heroi, critico_heroi = p1.atacar(monstro)
        print("Voce atacou o goblin!")
        if critico_heroi:
            print("DANO CRITICO")
        print(dano_heroi) 
        print(monstro.status()) 
        print("-" * 25)
        if not monstro.esta_vivo():
            print("Voce derrotou o goblin!!")
            break

    elif menu == "2":
        #Heroi se curando
        cura = p1.curar()
        print(f"Voce curou {cura} de vida")    
        print(p1.status())
        print("-" * 25)

    #Monstro dando dano no Heroi
    dano_monstro, critico_monstro = monstro.atacar(p1)
    print("O goblin atacou voce!")
    if critico_monstro:
        print("DANO CRITICO")
    print(dano_monstro)
    print(p1.status())
    print("-" * 25)
    
    if not p1.esta_vivo():
        print("Voce foi derrotado! fim de jogo.")
        break