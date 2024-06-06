class Spesa:
    def __init__(self,  categoria, importo, data=None):
        self.categoria = categoria
        self.importo = importo
        self.data_contabilizzazione = data

    def __str__(self):
        return f"Categoria: {self.categoria}\nImporto: {self.importo} euro\nnella data {self.data_contabilizzazione}\n"
