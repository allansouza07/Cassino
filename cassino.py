import random
import time

def sorteio():
    elementos = "🍇" , "🍑" , "🍉", "🍈"
    print()
    print("🎰 GIRANDO A ROLETA... ")
    print()
    for c in range(0,15):
        elemento_um = random.choice(elementos)
        elemento_dois = random.choice(elementos)
        elemento_tres = random.choice(elementos)
        print(f"\r{elemento_um} | {elemento_dois} | {elemento_tres}", end='' , flush=True)
        time.sleep(0.1)

    if elemento_um == elemento_dois == elemento_tres:
        print()
        print("Parabéns! Você ganhou a aposta!")
    elif elemento_um == elemento_dois or elemento_um == elemento_tres or elemento_dois == elemento_tres:
        print()
        print("Foi por quase! Tente novamente!")
    else:
        print()
        print("Não foi dessa vez! Tente novamente!")

print("VEM QUE TA PAGANDO! ao apostar uma quantia e ganhar a aposta, receba o TRIPLO")
aposta = float(input("Deposite aqui seu dinheiro: R$"))
resultado = aposta * 3
confirmar = float(input(f"Você deseja confirmar a aposta? (retorno de R$ {resultado:.2f})\n [1] Sim \n [2] Não \n - "))
if confirmar == 1.0:
    sorteio()
elif confirmar ==2.0:
    print("Ok, aposta cancelada!")
else:
    print("Erro! Aposta cancelada.")
