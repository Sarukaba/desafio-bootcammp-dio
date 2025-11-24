from typing import TYPE_CHECKING
from desafio_class_banco.models.clientes import Cliente
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from desafio_class_banco.models.historico import Historico

class Conta(ABC):
    def __init__(self,id: int,agencia: str,cliente: Cliente, historico: "Historico"):
        self.id = id 
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico
        self._saldo = 0.0

    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
       if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
       self._saldo = valor

    @abstractmethod
    def nova_conta(self):
        pass
    
    def sacar(self,valor: float | int):
        from desafio_class_banco.models.transacoes import Saque
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            trasacao = Saque(valor)
            trasacao.registrar(self)
            return True
        else:
            return False

    def depositar(self,valor: float | int):
        if valor > 0:
            from desafio_class_banco.models.transacoes import Deposito
            self.saldo += valor
            transacao = Deposito(valor)
            transacao.registrar(self)
            return True
        else:
            return False

class ContaCorrente(Conta):
    def __init__(self, id, agencia, cliente, historico):
        super().__init__(id, agencia, cliente, historico)
        self.__limite = 1000.0
        self._limite_saque = 5
    
    def __repr__(self):
        return f"{self.id}, {self.agencia}, {self.cliente}, {self.historico}, {self.__limite}, {self._limite_saque}"
    @classmethod
    def nova_conta(cls, id, agencia, cliente):
        historico = Historico()
        nova_instancia_conta = cls(id, agencia, cliente, historico)
        cliente.adicionar_contas(nova_instancia_conta)
        return True
    
    @property
    def limite(self):
        return self.__limite

    @property
    def limite_saque(self):
        return self._limite_saque

    @limite_saque.setter
    def limite_saque(self,valor):
        self._limite_saque - valor
    def sacar(self, valor):
        super().sacar(valor)
        self._limite_saque -= 1

