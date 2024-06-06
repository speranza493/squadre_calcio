
from ..utils import *
from .CategoriaSpesa import *
from ..Squadra.SquadreRagruppate import *
import random
from .Spesa import *


class ragruppaSpese:

    def __init__(self, lista_squadre:  set[Squadra]):
        self.ragruppaSpese: {str: [Spesa]} = {}
        categorie = [CategoriaSpesa.STIPENDI_GIOCATORI, CategoriaSpesa.ACQUISTI_GIOCATORI,
                     CategoriaSpesa.STIPENDI_ALLENATORI, CategoriaSpesa.STRUTTURE_SPORTIVE,
                     CategoriaSpesa.VIAGGI_ALLOGGI, CategoriaSpesa.ALTRO]
        for squadra in lista_squadre:
            nome = squadra.nome
            list_spese: [Spesa] = []
            for _ in range(random.randint(5, 10)):
                # Sceglie una categoria random
                categoria = random.choice(categorie)
                # Sceglie un importo a caso tra 1000 e 10000
                importo = random.uniform(1000, 10000)
                # Crea una data che sia nel 2024
                data = f"{random.randint(
                    2010, 2024):02d}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
                spesa = Spesa(categoria, importo, data)
                list_spese.append(spesa)
            self.ragruppaSpese[nome] = list_spese

    def __str__(self):
        return self.ragruppaSpese
