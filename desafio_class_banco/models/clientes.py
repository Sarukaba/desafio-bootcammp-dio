from abc import ABC 
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from desafio_class_banco.models.contas import Conta
    from desafio_class_banco.models.transacoes import Transacao


class Cliente(ABC):
    def __init__(self, endereco :str, id_user: int):
        self.endereco = endereco
        self.contas = []
        self.id_user = id_user
        
    def adicionar_contas(self, conta: "Conta"):
        self.contas.append(conta)
        return True

    def realizar_transacao(self,conta: "Conta", transacao: "Transacao"):
        pass

class PessoaFisica(Cliente):
    def __init__(self, endereco, id_user, cpf: str, nome: str, data_nasc: str):
        super().__init__(endereco,id_user)
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc

    def __repr__(self):
        
        return f"{self.id_user}, {self.cpf}, {self.nome}, {self.idade}, {self.data_nasc}, {self.endereco}, {self.contas}"
    
    @property
    def idade(self):
        return 2025 - int(self.data_nasc[4:])
        
    
