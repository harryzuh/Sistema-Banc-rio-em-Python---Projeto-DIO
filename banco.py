menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        print("Depósito")

        depositar = float(input("Digite a quantidade a ser depositada: "))
        if depositar > 0:
            saldo += depositar
            print(f"Você depositou R${depositar}")
            extrato += f"R${depositar:.2f}\n"

    elif opcao == "s":
        print("Saque")

        sacar = float(input("Digite a quantidade que deseja sacar: "))
       
        if numero_saques == LIMITE_SAQUES:
            print("Você atigiu limite de saques diário.") 

        elif saldo < sacar:
            print("Você não tem saldo suficiente.")

        elif sacar > limite:
            print("AVISO: Você não tem permissão para fazer saques acima de R$500,00")

        else:
            print(f"Você sacou R${sacar:.2f}")
            saldo -= sacar
            numero_saques += 1
        
        if sacar > 0:    
            extrato += f"R${sacar:.2f}\n"
        
        

    elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
            
    
    elif opcao == "q":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")