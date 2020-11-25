import pandas as pd

def extaire_la_premiere_lettre(serie):
  # Récupère une Série en argument
  # Retourne une DataFrame (compatibilité Col.Trans)
  return pd.DataFrame(serie.str[0])