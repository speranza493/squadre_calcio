from ..utils import *
from .Squadra import *


class Squadreragruppate:

    def __init__(self, data_path=None) -> None:
        self.squadreRagruppate: set(Squadra) = set()
        if data_path != None:
            righe_file = load_cv(data_path)
            for id, riga in righe_file:
                squadra = Squadra(
                    riga["nome_squadra"], riga["allenatore"], riga["lubicazione"])
                self.squadreRagruppate.add(squadra)
        print(self.squadreRagruppate)

    def __iter__(self):
        return self.squadreRagruppate.__iter__()

    def __str__(self):
        return self.squadreRagruppate
