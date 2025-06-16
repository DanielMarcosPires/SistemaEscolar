class Sala:
    def __init__(self, turma,serie):
        self._turma = turma
        self._serie = serie
        
    def get_turma(self):
        return f"Turma: {self._turma}"
    
    def get_serie(self):
        return f"Série: {self._serie}"