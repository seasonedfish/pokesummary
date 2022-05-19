#!/usr/bin/env python3
import pandas as pd
import csv


def main():
    df = pd.read_csv("type_defenses_original.csv", index_col=0)
    df.index = df.index.str.title()
    df.columns = df.columns.str.title()
    df = df.rename(
        columns={column: row
                 for column, row in zip(df.columns, df.index)}
    )
    df = df.fillna(1.0)
    df = df.replace("½", 0.5)
    df = df.astype(float)

    df = df.transpose()
    df.index.name = "defending_type"

    df.to_csv("type_defenses_modified.csv", quoting=csv.QUOTE_NONNUMERIC)


if __name__ == "__main__":
    main()
