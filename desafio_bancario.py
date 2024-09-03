import os

menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def deposito(value):
    if value < 0:
        limpar_terminal()
        return "valor negativo"
    global saldo, extrato
    saldo += value
    extrato += f"Deposito de R${value:.2f}.\n "
    limpar_terminal()
    return f"saldo depositado: R${value:.2f} saldo transacional R${saldo:.2f}"

def saque(value):
    if value > 500:
        limpar_terminal()
        return "valor muito alto para saque, faça um saque menor."
    global numero_saques, saldo, extrato
    if numero_saques >= LIMITE_SAQUES:
        limpar_terminal()
        return "limite de saque diario estourado"
    if saldo <= 0 or saldo < value:
        limpar_terminal()
        return "Saldo insuficiente"

    saldo -= value
    numero_saques += 1
    extrato += f"Saque de R${value:.2f}.\n"

    limpar_terminal()
    return f"saldo sacado: R${value:.2f}, saldo transacional R${saldo:.2f}."

def list_extrato():
    print(f" ================= EXTRATO ==================")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\n\nSaldo: R${saldo:.2f} ")
    print("==============================================")

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        value = float(input("Informe o valor de Deposito => "))
        print(deposito(value))

    elif opcao == "s":
        print("Saque")
        value = float(input("Informe o valor de Saque => "))
        print(saque(value))

    elif opcao == "e":
        print("extrato")
        list_extrato()

    elif opcao == "q":
        limpar_terminal()
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")