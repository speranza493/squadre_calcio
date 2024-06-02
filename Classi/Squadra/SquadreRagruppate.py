from ..utils import *
from .Squadra import *

class Squadreragruppate:
    
    def __init__(self, data_path = None) -> None:
        self.squadreRagruppate = set()
        if data_path != None:
            righe_file = load_cv(data_path)
            for id,riga in righe_file:
                squadra = Squadra(riga["id_squadra"],riga["nome_squadra"])
                self.squadreRagruppate.add(squadra)
                
                
    def __str__(self):
        return self.squadreRagruppate