import pandas as pd

"""
This module removes the extra quotation marks from
the original pokemon database (pokemon.csv)
and writes to a modified database (pokemon_modified.csv).
It is not used when the main program is executed
because the main program reads from modified database.
"""

if __name__ == "__main__":
    # Open from file
    df = pd.read_csv("pokemon.csv")
    # Get string columns
    df_string_cols = df.select_dtypes(include="object")
    # Remove leading and trailing quotation marks from string columns
    df_string_cols = df_string_cols.apply(
        lambda s: s.str.slice(start=1, stop=-1)
        if s.str.startswith("\"").any() & s.str.endswith("\"").any()
        else s
    )
    # Modify in place
    df.update(df_string_cols)
    # Write to file
    df.to_csv("pokemon_modified.csv", index=False)
