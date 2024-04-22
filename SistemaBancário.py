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

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
        else:
            print("Operação inválida, valor menor que 0.")
            
    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        if valor > 0 and numero_saques < LIMITE_SAQUES and valor <= limite:
            if valor <= saldo:
                saldo -= valor
                extrato += f"Saque de R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Não foi possível sacar o dinheiro por falta de saldo.")
        else:
            print("Operação inválida.")
            
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por usar o nosso banco. Até logo!")
        break
    
    else:
        print("Operação inválida.")
