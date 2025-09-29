import sys

import pandas as pd

def main():
  df = pd.read_csv("C:/Users/HomePC/Downloads/FAOSTAT_data_7-23-2022.csv")
  df = df[df["Area"].isin(["Ghana", "Côte d'Ivoire"])]
  df = df[df["Element"].isin(["Area harvested", "Yield", "Production"])]

  df_pivot = df.pivot_table(
    index=["Area", "Year"],
    columns="Element",
    values="Value"
  ).reset_index()

  df_pivot.columns.name = None
  df_pivot.rename(columns={
    "Area": "Country"
  }, inplace=True)

  ghana_data = df_pivot[df_pivot["Country"] == "Ghana"]
  print("\nGhana Cocoa Data")
  print(ghana_data.head())

  ivory_data = df_pivot[df_pivot["Country"] == "Côte d'Ivoire"]
  print("\nIvory Coast Cocoa Data")
  print(ivory_data.head())

if __name__ == "__main__":
    main()
    sys.exit(0)





