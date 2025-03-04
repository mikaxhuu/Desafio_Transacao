from datetime import datetime, date
import textwrap

usuarios = {

    "Cliente" : {"Agência": "", "Conta": "", "Saldo": ""}, 
}

opcao = ""
LIMITE_TRANSACAO = 10
qntd_transacao = 0
data_hora = datetime.now()
data_hoje = date.today()
mascara_ptbr = "%d/%m/%Y %H:%M"
extrato = ""

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

    cliente_registrado = {"Nome": {nome}, "Agência": {agencia}, "Conta" : {num_conta}, "Saldo": 0.0}

    print()

    return "Conta registrada com sucesso!"


def acessar_conta(nome_busca):

    nome_busca = input("\nDigite o nome da sua conta: ")

    for nome, nome_busca in usuarios:

        usuarios.get(nome_busca, {})

    print()

    return "Busca feita!"

def deposito(valor_deposito):

    valor_deposito = float(input("\nInforme o valor para ser depositado: "))

    saldo = usuarios["Saldo"]

    if valor_deposito > 0:

        if qntd_transacao < LIMITE_TRANSACAO:

            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f} ás {data_hora.strftime(mascara_ptbr)}\n"
            qntd_transacao + 1
            print("Saque realizado com sucesso!")
            print()

        elif qntd_transacao == LIMITE_TRANSACAO:

            print("\nVocê atingiu o limite de transações!")
            print()

    else:
        print("Operação falhou! O valor informado é inválido.")
        print()

def sacar(valor_saque):

    valor_saque = float(input("\nInforme o valor para ser sacado: "))

    saldo = usuarios["Saldo"]

    if valor_saque <= saldo and valor_saque > 0:

        if qntd_transacao < LIMITE_TRANSACAO:

            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f} ás {data_hora.strftime(mascara_ptbr)}\n"
            qntd_transacao + 1
            print("Saque realizado com sucesso!")
            print()

        elif qntd_transacao == LIMITE_TRANSACAO:

            print("\nVocê atingiu o limite de transações!")
            print()

    if valor_saque > saldo:

        print("\nVocê não tem saldo o suficiente!")
        print()

def exibir_extrato():

    saldo = usuarios["Saldo"]
    
    print("================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f} ás {data_hora.strftime(mascara_ptbr)}\n")
    print()

def main():

    usuarios["Cliente"]

    while True:
        print = (f"\nHoje é dia {data_hoje}")
        opcao = menu()

        if opcao == "d":

            valor = float(input(deposito(valor)))

        elif opcao == "s":

            valor = float(input(sacar(valor)))

        elif opcao == "e":

            exibir_extrato()

        elif opcao == "r":

            registrar_conta()

        elif opcao == "a":

            nome_busca = input("\nDigite o nome da conta: ")

            acessar_conta(nome_busca)

        elif opcao == "q":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")



main()