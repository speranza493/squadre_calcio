from .Spesa import *
from ..utils import *

class ragruppaSpese:
    
    def __init__(self, path_file = None):
        self.ragruppaSpese = []
        if path_file != None:
            righe_file = load_cv(path_file)
            for id,riga in righe_file:
                spesa = Spesa(riga["id_squadra"],riga["categoria_spesa"],riga["importo"],riga["data_contabilizzazione"])
                self.ragruppaSpese.append(spesa)
                
    def __str__(self):
        return self.ragruppaSpese
                
                
        