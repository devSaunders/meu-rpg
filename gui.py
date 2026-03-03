import tkinter as tk 
from personagens import Heroi, Monstro
from combate import iniciar_batalha, passo_batalha

janela = tk.Tk()
janela.title("RPG POG")

heroi = Heroi("Jogador", 100, 10)
inimigo = Monstro("Goblin", 80, 8)

state = iniciar_batalha(heroi, inimigo)
print(state)

status = tk.Label(janela, text="")
status.pack()
log = tk.Text(janela, height=15, width=60)
log.pack()

def atualizar_status():
    texto = f"{heroi.nome}: {heroi.vida}/{heroi.vida_max} HP\n"
    texto += f"{inimigo.nome}: {inimigo.vida}/{inimigo.vida_max} HP\n"
    status.config(text=texto)

def acao(acao_str):
    resultado = passo_batalha(state, acao_str)
    texto = "\n".join(resultado["mensagens"])
    log.insert("end", texto + "\n")
    atualizar_status()

tk.Button(janela, text="atacar", command=lambda: acao("atacar")).pack()
tk.Button(janela, text="curar",command=lambda: acao("curar")).pack()
tk.Button(janela, text="defender",command=lambda: acao("defender")).pack()
tk.Button(janela, text="ataque especial",command=lambda: acao("ataque especial")).pack()


atualizar_status()

janela.mainloop()