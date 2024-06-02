class Spesa:
    def __init__(self, categoria, importo):
        self.categoria = categoria
        self.importo = importo

    def __str__(self):
        return f"Categoria: {self.categoria}\nImporto: {self.importo} euro\n"