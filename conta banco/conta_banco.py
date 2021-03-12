def conta_banco(numero, nome, saldo, limite):
    conta = {"Numero":numero, "nome":nome, "saldo":saldo, "limite":limite}
    return conta

def depositar(conta, valor):
    conta ["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))


conta = conta_banco(123, "gadotti", 100.0, 500.0)
print("saldo na conta {} ".format(conta["saldo"]))
valor = int(input("Digite um valor de deposito: "))
depositar(conta, valor)
print("saldo na conta {} ".format(conta["saldo"]))
valor = valor = int(input("Digite um valor de saque: "))
sacar(conta, valor)
print("saldo na conta {} ".format(conta["saldo"]))
