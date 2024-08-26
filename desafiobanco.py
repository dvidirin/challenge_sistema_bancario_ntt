def menu():
    print("\n--- Sistema Bancário ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

def depositar(saldo, extrato):
    valor = float(input("Informe o valor para depósito: R$ "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito!")
    return saldo, extrato

def sacar(saldo, extrato, saques_diarios, limite_saques=3, limite_saque=500):
    if saques_diarios < limite_saques:
        valor = float(input("Informe o valor para saque: R$ "))
        if valor > saldo:
            print("Saldo insuficiente para realizar saque!")
        elif valor > limite_saque:
            print(f"O limite para saque é de R$ {limite_saque:.2f} por operação!")
        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            saques_diarios +=1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque!")
    else:
        print("Limite diário de saques atingido!")
    return saldo, extrato, saques_diarios

def exibir_extrato(saldo, extrato):
    print("\n--- Extrato ---")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

def main():
    saldo = 0
    extrato = []
    saques_diarios = 0

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, saques_diarios = sacar(saldo, extrato, saques_diarios)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__=="__main__":
    main()        