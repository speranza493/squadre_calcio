from ..utils import *
from .Squadra import *


class Squadreragruppate:
    # in questa classe inserisco tutti i valori del csv dentro un insime di Oggetti Squadra

    def __init__(self, data_path=str | None) -> None:
        self.squadreRagruppate: set[Squadra] = set()
        if data_path != None:
            righe_file = load_cv(data_path)
            for id, riga in righe_file:
                squadra = Squadra(
                    riga["nome_squadra"], riga["allenatore"], riga["lubicazione"])
                self.squadreRagruppate.add(squadra)

    def __iter__(self):
        return self.squadreRagruppate.__iter__()

    def __str__(self):
        return self.squadreRagruppate
