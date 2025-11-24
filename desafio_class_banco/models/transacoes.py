from abc import ABC, abstractmethod
from desafio_class_banco.models.contas import Conta

class Transacao(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def registrar(self, conta: Conta):
        pass

class Saque(Transacao):
    def __init__(self,valor):
        self.valor = valor
    
    def registrar(self,conta: Conta):
        conta.historico.adicionar_transacao(self)

    def __repr__(self):
        return f"Saque(valor={self.valor})"
class Deposito(Transacao):
    def __init__(self,valor):
        self.valor = valor
    
    def __repr__(self):
        return f"Deposito(valor={self.valor})"
    
    def registrar(self,conta: Conta):
        conta.historico.adicionar_transacao(self)