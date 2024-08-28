def menu():
    print("\n--- Sistema Bancário ---")
    print("1. Criar Usuário")
    print("2. Criar Conta Corrente")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Extrato")
    print("6. Sair")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Já existe um usuário com esse CPF!")
        return usuarios
    
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})
    print("Usuário criado com sucesso!")
    return usuarios

def criar_conta_corrente(contas, usuarios):
    cpf = input("Informe o CPF do usuário para vincular à conta: ")
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if usuario:
        numero_conta = len(contas) + 1
        agencia = "0001"
        contas.append({"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario})
        print(f"Conta Corrente criada com sucesso! Agência: {agencia} | Número da conta: {numero_conta}")
    else:
        print("Usuário não encontrado. Certifique-se de que o CPF está correto.")
    
    return contas

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
    usuarios = []
    contas = []
    saldo = 0
    extrato = []
    saques_diarios = 0

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuarios = criar_usuario(usuarios)
        elif opcao == "2":
            contas = criar_conta_corrente(contas, usuarios)
        elif opcao == "3":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "4":
            saldo, extrato, saques_diarios = sacar(saldo, extrato, saques_diarios)
        elif opcao == "5":
            exibir_extrato(saldo, extrato)
        elif opcao == "6":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()        