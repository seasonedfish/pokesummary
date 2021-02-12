import pkgutil
import pandas as pd
from io import BytesIO

if __name__ == "__main__":
    data = pkgutil.get_data(__name__, "data/pokemon.csv")
    df = pd.read_csv(BytesIO(data))
