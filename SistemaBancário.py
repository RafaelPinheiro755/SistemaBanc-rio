def menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    => """

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação inválida, valor menor que 0.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > 0 and numero_saques < LIMITE_SAQUES and valor <= limite:
        if valor <= saldo:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Não foi possível sacar o dinheiro por falta de saldo.")
    else:
        print("Operação inválida.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios): 
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nUsuário já cadastrado com esse CPF!")
        return
    nome = input("Informe nome de usuário completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, fluxo de criação de conta encerrado: ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)

def main():
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    usuarios = []
    contas = []

    while True:

        opcao = input(menu())

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor de saque: "))
            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Obrigado por usar o nosso banco. Até logo!")
            break
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
            
        else:
            print("Operação inválida.")

main()
