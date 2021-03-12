def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}


def depositar(conta, valor):
    conta["saldo"] += valor


def sacar(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("saldo {}".format(conta["saldo"]))

sacar()
depositar()
criar_conta()
extrato()
