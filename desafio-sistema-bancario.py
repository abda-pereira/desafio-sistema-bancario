menu = """

================ SISTEMA BANCÁRIO ================

Escolha uma operação que deseja realizar:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

==================================================

=> """

submenu = """

=================================================

Escolha uma opção:

[1] Voltar para o menu principal
[2] Sair

=================================================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def exibir_submenu():
    while True:
        opcao_submenu = input(submenu)
        if opcao_submenu == "1":
            return True
        elif opcao_submenu == "2":
            return False
        else:
            print("\nOpção inválida! Por favor, selecione novamente.")

while True:

    opcao = input(menu)

    if opcao == "1":
        try:
            valor = float(input("\nInforme o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("\nOperação falhou! O valor informado é inválido.")

        except ValueError:
            print("\nOperação falhou! O valor informado não é um número válido.")

        if not exibir_submenu():
            break

    elif opcao == "2":
        try:
            valor = float(input("\nInforme o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("\nOperação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("\nOperação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("\nOperação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

                print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("\nOperação falhou! O valor informado é inválido.")

        except ValueError:
            print("\nOperação falhou! O valor informado não é um número válido.")

        if not exibir_submenu():
            break

    elif opcao == "3":
        print("\n==================== EXTRATO ====================")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        # print("\n=================================================")

        if not exibir_submenu():
            break

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
