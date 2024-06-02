class Stadio:
    def __init__(self, nome, capacita, citta, indirizzo):
        self.nome = nome
        self.capacita = capacita
        self.citta = citta
        self.indirizzo = indirizzo
        
    def __init__(self,nome):
        self.nome = nome
        

    def __str__(self):
        return f"Stadio: {self.nome}\nCittà: {self.citta}\nIndirizzo: {self.indirizzo}\nCapacità: {self.capacita}\n"