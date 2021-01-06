import pandas as pd

daily_df = pd.read_csv("data/daily_report.csv")

totals_df = daily_df[["Confirmed", "Deaths", "Recovered"]
                     ].sum().reset_index(name="count")
totals_df = totals_df.rename(columns={"index": "condition"})


countries_totals = daily_df[["Country_Region",
                             "Confirmed", "Deaths", "Recovered"]]
countries_totals = countries_totals.groupby(
    "Country_Region").sum().reset_index()
