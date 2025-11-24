# importa classes/funções usando caminho absoluto
from desafio_class_banco.models.clientes import PessoaFisica
from desafio_class_banco.models.contas import ContaCorrente
from desafio_class_banco.models.transacoes import Deposito, Saque
from desafio_class_banco.models.historico import Historico

# controla o que aparece em "from models import *"
__all__ = [
    "PessoaFisica",
    "ContaCorrente",
    "Deposito",
    "Saque",
    "Historico",
]
