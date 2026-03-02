from personagens import Heroi, Monstro, Orc
from combate import iniciar_batalha, passo_batalha

def recompensas(heroi): #dando recompensas para o heroi pos turno
    heroi.cooldown = 0
    print("Seu cooldown foi resetado!")
    cura = int(heroi.vida_max * 0.4)
    antes = heroi.vida
    heroi.vida = heroi.vida + cura
    if heroi.vida > heroi.vida_max:
        heroi.vida = heroi.vida_max
    cura_real = heroi.vida - antes
    print(f"Voce recuperou {cura_real}, agora sua vida é {heroi.vida}/{heroi.vida_max}!")

def main():
    goblin = Monstro("goblin", 80, 8)
    orc = Orc("Orc", 120, 12)
    nome = input("informe o nome do seu personagem: ")
    print("-" * 25)
    inimigos = [goblin, orc]
    p1 = Heroi(nome, 100, 10)
    
    for inimigo in inimigos: 
        print(f"Um {inimigo.nome} apareceu!!")
        #batalha(p1, inimigo)
        
        state = iniciar_batalha(p1, inimigo)
        while not state["acabou"]:
            print("""1 - atacar
                    2 - curar
                    3 - defender
                    4 - especial""")
            acao = input("escolha uma acao: ")
            if acao == "1":
                acao = "atacar"
            elif acao == "2":
                acao = "curar"
            elif acao == "3":
                acao = "defender"
            elif acao == "4":
                acao = "ataque especial"
            resultado = passo_batalha(state, acao)
            for msg in resultado["mensagens"]:
                print(msg)
        
        if not p1.esta_vivo():
            break
        else: 
            recompensas(p1)
            print("-" * 25)
    if p1.esta_vivo():
        print("VOCE VENCEU TODAS AS FASES!!")
    else:
        print("FIM DE JOGO!")

if __name__ == "__main__":
    main()
