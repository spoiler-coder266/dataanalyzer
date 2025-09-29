import sys

import pandas as pd
import matplotlib.pyplot as plt

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
  df_pivot.rename(columns={"Area": "Country"}, inplace=True)

  df_pivot.sort_values(by=["Country", "Year"], inplace=True

  ghana_data = df_pivot[df_pivot["Country"] == "Ghana"]
  ivory_data = df_pivot[df_pivot["Country"] == "Côte d'Ivoire"]


  def plot_country_data(data, country_name, emoji):
     plt.figure(figsize=(10, 6))
     plt.plot(data["Year"], data["Area harvested"], label="Area harvested (ha)", marker='o')
     plt.plot(data["Year"], data["Production"], label="Production (tonnes)", marker='s')
     plt.plot(data["Year"], data["Yield"], label="Yield (hg/ha)", marker='^')
     plt.title(f"{emoji} {country_name} - Cocoa Data Over Time", fontsize=14)
     plt.xlabel("Year")
     plt.ylabel("Value")
     plt.grid(True)
     plt.legend()
     plt.tight_layout()
     plt.show()

  plot_country_data(ghana_data, "Ghana" )

  plot_country_data(ivory_data, "Côte d'Ivoire")

  if __name__ == "__main__":
  main()
  sys.exit(0)

