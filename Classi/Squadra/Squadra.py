from ..Spese.Spesa import *


class Squadra:
    def __init__(self,  nome: str, allenatore: str, lubicazione: str):
        self.nome = nome
        self.allenatore = allenatore
        self.lubicazione = lubicazione

    def __str__(self):
        return f"Squadra: {self.nome} allenatore: {self.allenatore} e lubicazione: {self.lubicazione}"
