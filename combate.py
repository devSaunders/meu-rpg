def batalha(heroi, inimigo):
    while heroi.esta_vivo() and inimigo.esta_vivo(): #isso faz a verificacao se o turno acabou ou nao/faz a conta do cooldown da habilidade especial
        
        if heroi.cooldown > 0:
            heroi.cooldown -= 1
        print(heroi.status())
        print(inimigo.status())
        print("-" * 25)
        menu = input("""O que voce deseja fazer agora? 
        1. Atacar 
        2. Curar
        3. Defender
        4. Ataque especial """)
        print("-" * 25)
        
        while menu != "1" and menu != "2" and menu != "3" and menu != "4": 
            print("Opcao invalida!")
            menu = input("O que voce deseja fazer? ")
            print("-" * 25)

        if menu == "1":
            #Heroi dando dano no Inimigo
            dano_heroi, critico_heroi = heroi.atacar(inimigo)
            print(f"Voce atacou o {inimigo.nome}!")
            if critico_heroi:
                print("DANO CRITICO")
            print(dano_heroi) 
            print(inimigo.status()) 
            print("-" * 25)

        elif menu == "2":
            #Heroi se curando
            cura = heroi.curar()
            print(f"Voce curou {cura} de vida")    
            print(heroi.status())
            print("-" * 25)

        elif menu == "3":
            #Heroi defendendo
            heroi.defender()
            print(f"Voce se denfendeu do {inimigo.nome}!")
            print(heroi.status())
            print("-" * 25)
        
        elif menu == "4":
            #Heroi dando ataque especial
            dano, usou = heroi.ataque_especial(inimigo)
            if usou:
                print("voce usou seu ataque especial")
                print(dano)  
                print(inimigo.status())
                print("-" * 25)
            else:
                print(f"Habilidade em cooldown: {heroi.cooldown}")  
                continue
            
        #Monstro dando dano no Heroi
        if not inimigo.esta_vivo():
            print(f"Voce derrotou o {inimigo.nome}!!")
            break
        dano_monstro, critico_monstro = inimigo.atacar(heroi)
        print(f"O {inimigo.nome} atacou voce!")
        print(dano_monstro)
        print(heroi.status())
        print("-" * 25)
        if not heroi.esta_vivo():
            print("Voce foi derrotado! fim de jogo.")
            break