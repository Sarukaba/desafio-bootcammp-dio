from desafio_class_banco.models.transacoes import Transacao

class Historico:
    def __init__(self):
        self.historico = []
    
    def __repr__(self):
        return f"Historico(transacoes={self.historico})"
    
    def adicionar_transacao(self,transacao : Transacao):
        self.historico.append(transacao)
        