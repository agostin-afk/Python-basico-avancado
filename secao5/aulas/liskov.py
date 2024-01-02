from abc import abstractmethod, ABC

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool:
        ...
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail. Enviando: ', self.mensagem)
        return True
        
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS. Enviando: ', self.mensagem)
        return True
        
        
def notificar(mensagem:Notificacao):
    notificacao_enviada = mensagem.enviar()
    if notificacao_enviada:
        print('Notificacao enviada')
    else:
        print('Notificacao não enviada.')
        
notificar(NotificacaoEmail('testando e-mail'))