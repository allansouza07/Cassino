import random
import time
import funcoes_banco

#AREA DE LOGIN E CADASTRO
banco = "banco_dados.txt"

funcoes_banco.abrir_banco(banco)

print("Bem-vindo ao cassino virtual!")
#FUNCAO LOGIN
def login():
    print("-"*60)
    print(f"{" "*20}Área de login")
    print("-"*60)

    while True:
        try:
            nome = str(input("Digite seu nome: "))
            senha = input("Digite sua senha: ")
        except ValueError:
            print("DIgite o nome de usuário sem números")
            continue
        else:
            if funcoes_banco.analisar(banco, nome, senha):
                print("Acesso liberado!")
                break
            else:
                print("Usuário ou senha digitados de maneira incorreta!")
                escolha = int(input("Não tem cadastro? Crie uma conta! \n [1]Ir para área de cadastro \n [2]Tentar novamente"))
                if escolha == 1:
                    cadastro_cli()
                elif escolha == 2:
                    continue
                else:
                    print("erro! Tente novamete.")
                continue
#FUNCAO CADASTRO
def cadastro_cli():     
        print("-"*60)
        print( f"{" "*20}ÁREA DE CADASTRO")
        print("-"*60)
        while True:
            try: 
                nome = str(input("digite seu nome: "))
                idade = int(input("digite sua idade: "))
                senha = input("cadastre uma senha: ")
            except ValueError:
                print("Escreva o dado corretamente")
            else:
                if idade <18:
                    print("Proibido para menores de idade!")
                    continue
                else:
                    break

        dic = {"nome": nome, "senha": senha, "idade": idade}
        print(f"Usuário {dic["nome"]} cadastrado em nosso sistema!")
        funcoes_banco.cadastrar(banco, nome, senha)
        return nome

while True:
    try:
        cadastro = int(input("Você já possuí cadastro em nosso sistema? \n [1]Sim \n [2]Não \n - "))
    except:
        print("Digite um número inteiro")
        continue
    else:
        if cadastro>2 :
            print("digite 1 ou 2!")
            continue
        else: 
            break
if cadastro ==1:
    login()
elif cadastro == 2:
    cadastro_cli()
    login()



def sorteio():
    elementos = "🍇" , "🍑" , "🍉","🍍","🍒"
    elementos_especiais = "🍍"
    elemento_coringa = "🍒"
    print()
    print("🎰 GIRANDO A ROLETA... ")
    print()
    for c in range(0,15):
        elemento_um = random.choice(elementos)
        elemento_dois = random.choice(elementos)
        elemento_tres = random.choice(elementos)
        print(f"\r{elemento_um} | {elemento_dois} | {elemento_tres}", end='' , flush=True)
        time.sleep(0.1)

    while True:
        if elemento_um == "🍍" and elemento_dois == "🍍" and elemento_tres =="🍍":
            print()
            print("Parabéns, você ganhou a aposta triplicada!")
            print(f"Em breve, R$ {valor_aposta * 3} serão depositados em sua conta!")
            break
        elif elemento_um == elemento_dois == elemento_tres:
            print()
            print("Parabéns! Você ganhou a aposta!")
            print(f"Em breve, R$ {valor_aposta * 2} serão depositados em sua conta!")
            break

        elif elemento_um == elemento_dois and elemento_tres=="🍒" or elemento_um =="🍒" and elemento_dois == elemento_tres or elemento_um == "🍒" and elemento_dois == elemento_tres:
            print()
            print("Parabéns! Você ganhou a aposta!")
            print(f"Em breve, R$ {valor_aposta * 2} serão depositados em sua conta!")
            break
        elif elemento_um =="🍒" and elemento_dois=="🍒" or elemento_dois == "🍒" and elemento_tres=="🍒" or elemento_tres == "🍒" and elemento_um=="🍒" or elemento_um == "🍒" and elemento_dois =="🍒" and elemento_tres=="🍒":
            print()
            print("Parabéns! Você ganhou a aposta!")
            print(f"Em breve, R$ {valor_aposta * 2} serão depositados em sua conta!")
            break

        elif elemento_um == elemento_dois or elemento_um == elemento_tres or elemento_dois == elemento_tres:
            print()
            print("Foi por quase! Tente novamente!")
            break
        else:
            print()
            print("Não foi dessa vez! Tente novamente!")
            break


print()
def aposta():
    print("Ao apostar uma quantia e ganhar a aposta, tenha a chance de receber o TRIPLO do que apostou!")
    print()
    print("-------------------- ODDS --------------------")
    print("Frutas com valores comuns: 🍇, 🍑, 🍉  ")
    print("Fruta com valor especial: 🍍")
    print("Fruta coringa: 🍒")
    print()
    apostaa = float(input(f"Deposite aqui seu dinheiro : R$"))
    resultado = apostaa * 2
    resultado_triplo = apostaa * 3
    confirmar = float(input(f"Você deseja confirmar a aposta? (retorno de R$ {resultado:.2f} em caso de resultado normal e R$ {resultado_triplo:.2f} em caso de resultado especial)\n [1] Sim \n [2] Não \n - "))
    if confirmar == 1.0:
        sorteio()
    elif confirmar ==2.0:
        print("Ok, aposta cancelada!")
    else:
        print("Erro! Aposta cancelada.")
    
    return apostaa


valor_aposta= aposta()
print(valor_aposta)





def continuar():
    valor_aposta = None
    while True:
        continuar=float(input("Quer fazer outra aposta?\n [1] Sim\n [2] Não \n - "))
        if continuar==1.0:
            valor_aposta = aposta()
            return valor_aposta
        else:
            break
continuar()

print("Obrigado por jogar, volte sempre!")