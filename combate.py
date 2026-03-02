def batalha(heroi, inimigo):
    while heroi.esta_vivo() and inimigo.esta_vivo(): #isso faz a verificacao se o turno acabou ou nao/faz a conta do cooldown da habilidade especial
        
        if heroi.cooldown > 0:
            heroi.cooldown -= 1
        print(heroi.status())
        print(inimigo.status())
        menu = input("""O que voce deseja fazer agora? 
        1. Atacar 
        2. Curar
        3. Defender
        4. Ataque especial """)
        
        while menu != "1" and menu != "2" and menu != "3" and menu != "4": 
            print("Opcao invalida!")
            menu = input("O que voce deseja fazer? ")

        if menu == "1":
            resultado = turno_heroi(heroi, inimigo, "atacar")
            for msg in resultado["mensagens"]:
                print(msg)
            
        elif menu == "2":
            resultado = turno_heroi(heroi, inimigo, "curar")
            for msg in resultado["mensagens"]:
                print(msg)

        elif menu == "3":
            resultado = turno_heroi(heroi, inimigo, "defender")
            for msg in resultado["mensagens"]:
                print(msg) 

        elif menu == "4":
            resultado = turno_heroi(heroi, inimigo, "ataque especial")
            for msg in resultado["mensagens"]:
                print(msg)
    
        if resultado["inimigo_morreu"]:
            break
        if not resultado["turno_consumido"]:
            continue

        #Monstro dando dano no Heroi
        resultado = turno_inimigo(heroi, inimigo)
        for msg in resultado["mensagens"]:
            print(msg)
        if resultado["heroi_morreu"]:
            break

def turno_heroi(heroi, inimigo, acao):
    mensagens = []
    turno_consumido = True
    if acao == "atacar":
        dano, critico = heroi.atacar(inimigo)
        mensagens.append("voce atacou!")
        mensagens.append(f"voce deu {dano} de dano no inimigo!")
        if critico:
            mensagens.append("DANO CRITICO")
    
    elif acao == "curar":
        vida_max = heroi.vida_max
        vida_antes = heroi.vida
        cura = int(heroi.vida_max * 0.2)
        heroi.vida += cura
        if heroi.vida > vida_max:
            heroi.vida = vida_max
        cura_total  = heroi.vida - vida_antes    
        mensagens.append(f"Voce curou {cura_total} pontos de vida")
        mensagens.append(f"HP: {heroi.vida}/{heroi.vida_max}")
        turno_consumido = True

    elif acao == "defender":
        heroi.defendendo = True 
        mensagens.append("Voce defendeu!")
    
    elif acao == "ataque especial":
        if heroi.cooldown > 0:
            mensagens.append(f"Faltam {heroi.cooldown} turnos para o Ataque Especial.")
            turno_consumido = False
        else:

            dano = heroi.ataque_especial(inimigo)
            mensagens.append("Voce usou seu ataque especial!")
            mensagens.append(f"Voce deu {dano} de dano!")

    else: 
        mensagens.append("Acao invalida!")
        turno_consumido = False
    
    if turno_consumido:
        heroi.cooldown -= 1
    
    return {
        "mensagens": mensagens,
        "turno_consumido": turno_consumido,
        "inimigo_morreu": not inimigo.esta_vivo()
    }
    
def turno_inimigo(heroi, inimigo):
    
    mensagens = []
    dano = inimigo.atacar(heroi)
    mensagens.append(f"o {inimigo.nome} atacou voce!")
    
    return{
        "mensagens": mensagens, 
        "heroi_morreu": not heroi.esta_vivo()
    }
    
def iniciar_batalha(heroi, inimigo):
    return {
        "heroi": heroi,
        "inimigo": inimigo,
        "acabou": False,
        "vencedor": None   
    }
    
def passo_batalha(state, acao):
    mensagens = []
    turno_consumido = False
    if state["acabou"]:
        mensagens.append("A batalha acabou")
    else:
        heroi = state["heroi"]
        inimigo = state["inimigo"]
        r_heroi = turno_heroi(heroi, inimigo, acao) #isso retorna a dict
        mensagens.extend(r_heroi["mensagens"])
        turno_consumido = r_heroi["turno_consumido"]
        if r_heroi["inimigo_morreu"]:
            state["acabou"] = True
            state["vencedor"] = "heroi"
        if (not state["acabou"]) and turno_consumido:
            r_inimigo = turno_inimigo(heroi, inimigo)
            mensagens.extend(r_inimigo["mensagens"])
            if r_inimigo["heroi_morreu"]:
                state["acabou"] = True
                state["vencedor"] = "inimigo"                
     

    return {
        "mensagens": mensagens,
        "turno_consumido": turno_consumido,
        "acabou": (state["acabou"]),
        "vencedor": (state["vencedor"])
    }