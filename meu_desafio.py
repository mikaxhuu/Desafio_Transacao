from datetime import datetime, date
import textwrap

usuarios = {}

LIMITE_TRANSACAO = 10
mascara_ptbr = "%d/%m/%Y %H:%M"

def menu():
    menu = """\n
    ================ MENU ================

    [r]\tRegistrar Conta
    [a]\tAcessar Conta
    [d]\tDepósito
    [s]\tSaque
    [e]\tExtrato
    [q]\tSair

    \n=> """
    return input(textwrap.dedent(menu))


def registrar_conta():
    nome = input("\nQual é o nome do cliente para ser registrado? ")
    agencia = input("\nDigite a agência (Exemplo: 00000-00): ")
    num_conta = input("\nDigite o número da conta (Exemplo: 0000): ")

    if nome in usuarios:
        print("Cliente já registrado!")
    else:
        usuarios[nome] = {"Agência": agencia, "Conta": num_conta, "Saldo": 0.0, "Transacoes": 0, "Extrato": ""}
        print("Conta registrada com sucesso!")


def acessar_conta(nome_busca):
    if nome_busca in usuarios:
        print(f"Conta encontrada: Agência {usuarios[nome_busca]['Agência']}, Conta {usuarios[nome_busca]['Conta']}")
    else:
        print("Conta não encontrada!")


def deposito(nome, valor_deposito):
    if nome in usuarios:
        if valor_deposito > 0:
            if usuarios[nome]["Transacoes"] < LIMITE_TRANSACAO:
                usuarios[nome]["Saldo"] += valor_deposito
                data_hora = datetime.now()
                usuarios[nome]["Extrato"] += f"Depósito: R$ {valor_deposito:.2f} às {data_hora.strftime(mascara_ptbr)}\n"
                usuarios[nome]["Transacoes"] += 1
                print("Depósito realizado com sucesso!")
            else:
                print("\nVocê atingiu o limite de transações!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Conta não encontrada!")


def sacar(nome, valor_saque):
    if nome in usuarios:
        if valor_saque > 0 and valor_saque <= usuarios[nome]["Saldo"]:
            if usuarios[nome]["Transacoes"] < LIMITE_TRANSACAO:
                usuarios[nome]["Saldo"] -= valor_saque
                data_hora = datetime.now()
                usuarios[nome]["Extrato"] += f"Saque: R$ {valor_saque:.2f} às {data_hora.strftime(mascara_ptbr)}\n"
                usuarios[nome]["Transacoes"] += 1
                print("Saque realizado com sucesso!")
            else:
                print("\nVocê atingiu o limite de transações!")
        else:
            print("Operação falhou! Saldo insuficiente ou valor inválido.")
    else:
        print("Conta não encontrada!")


def exibir_extrato(nome):
    if nome in usuarios:
        print("================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not usuarios[nome]["Extrato"] else usuarios[nome]["Extrato"])
        print(f"\nSaldo: R$ {usuarios[nome]['Saldo']:.2f} às {datetime.now().strftime(mascara_ptbr)}\n")
    else:
        print("Conta não encontrada!")


def main():
    while True:
        print(f"\nHoje é dia {date.today().strftime('%d/%m/%Y')}")
        opcao = menu()

        if opcao == "r":
            registrar_conta()

        elif opcao == "a":
            nome_busca = input("\nDigite o nome da conta: ")
            acessar_conta(nome_busca)

        elif opcao == "d":
            nome = input("\nDigite o nome da conta: ")
            valor = float(input("Informe o valor para ser depositado: "))
            deposito(nome, valor)

        elif opcao == "s":
            nome = input("\nDigite o nome da conta: ")
            valor = float(input("Informe o valor para ser sacado: "))
            sacar(nome, valor)

        elif opcao == "e":
            nome = input("\nDigite o nome da conta: ")
            exibir_extrato(nome)

        elif opcao == "q":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")


main()