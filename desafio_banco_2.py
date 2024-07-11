menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[q] Sair

=> """
usuarios = []
contas = []

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
AGENCIA = "0001"
LIMITE_SAQUES = 3

def depositar(valor, /):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Você depositou R${valor:.2f}\n")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, valor, limite, limite_saques):
    global saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n Operação falhou! O valor do saque escede o limite.")

    elif excedeu_limite:
        print("\n Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\n Operação falhou! Número máximo de saques excedido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nVocê sacou R${valor:.2f}")
    else:
        print("\n Operação falhou! O valor informado é invalido")

    return saldo, extrato, numero_saques

# def exibir_extrato(saldo, *, / extrato):
    pass

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios_filtrados.append(usuario)
    if usuarios_filtrados:
        return usuarios_filtrados[0]
    else:
        return None

def criar_usuario(usuario):
    cpf = input("Digite seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("Já existe usuário com esse CPF.")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("Usuário cadastrado!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("usuário não encontrado.")

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))    

        sacar(
            valor=valor,
            limite=limite,
            limite_saques=LIMITE_SAQUES,
            )   

    elif opcao == "3":
        exibir_extrato(saldo, extrato = extrato)

    elif opcao == "4":
        criar_usuario(usuarios)
    
    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta == True:
            contas.append(conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print(saldo)
print(numero_saques)
print(contas)
print(usuarios)