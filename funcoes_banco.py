def abrir_banco(arq):
    try:
        op = open(arq ,'rt')
        
    except FileNotFoundError:
        print("banco não encontrado.")
        return False
    else:
        print("banco encontrado!")
        print(op.readlines())
        return True

def cadastrar(arq, nome, senha):
    try:
        a = open(arq, "at")
    except:
        print("deu erro")
    else:
        a.write(f"{nome}|{senha}\n")
        print() 

def analisar(arq, nome, senha):
    try:
        with open (arq, 'rt') as banco:
            for c in banco:
                nome_arq, senha_arq = c.strip().split("|")

                if nome == nome_arq and senha == senha_arq:
                    return True
        return False
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return False