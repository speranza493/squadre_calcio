class Squadra:
    def __init__(self, id_, nome):
        self.nome = nome
        self.ID = id_

    def aggiungi_spesa(self, spesa):
        self.spese.append(spesa)

    def calcola_totale_spese(self):
        return sum(spesa.importo for spesa in self.spese)

    def __str__(self):
        return f"Squadra: {self.nome} id: {self.ID}"
