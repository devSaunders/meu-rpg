from personagens import Heroi, Monstro, Orc
from combate import batalha

def main():
    goblin = Monstro("goblin", 80, 8)
    orc = Orc("Orc", 120, 12)
    nome = input("informe o nome do seu personagem: ")
    print("-" * 25)
    inimigos = [goblin, orc]
    p1 = Heroi(nome, 100, 10)
    for inimigo in inimigos: 
        print(f"Um {inimigo.nome} apareceu!!")
        batalha(p1, inimigo)    
        if not p1.esta_vivo():
            break

if __name__ == "__main__":
    main()
