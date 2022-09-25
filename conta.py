class Conta:
    def __init__(self,titular: str,saldo: float = 0):
        self.titular = titular
        self._saldo = saldo

    
    @property
    def saldo(self) -> float:
        return self.__saldo
    
    @saldo.setter
    def depositar(self, novo_saldo) -> None:
            self.__saldo = novo_saldo
