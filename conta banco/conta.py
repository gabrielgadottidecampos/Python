class Conta:
    def __init__(self, numero, nome, saldo, limite):
        self.__numero = numero
        self.__titular = nome
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_a_sacar <=  valor_disponivel_saque

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O Valor {} é maior que o limite disponivel".format(valor))

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.limite
    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite
    @staticmethod
    def codigo_banco():
        return "001"
