class Spesa:
    def __init__(self,id_squadra, categoria, importo,data = None):
        self.categoria = categoria
        self.importo = importo
        self.id_squadra = id_squadra
        self.data_contabilizzazione = data
        

    def __str__(self):
        return f"Categoria: {self.categoria}\nImporto: {self.importo} euro\n"