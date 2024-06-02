import pandas as pd

from Classi.Squadra.Squadra import *


def load_cv(file_path):

    print(f"Tentativo di caricare il file CSV dal percorso: {file_path}")

    try:

        df = pd.read_csv(file_path, encoding = "utf-8").iterrows()

        return df

    except Exception as e:

        print(f"Errore durante il caricamento delle squadre: {e}")
        raise e