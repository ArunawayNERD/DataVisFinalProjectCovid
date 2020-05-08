import pandas as pd

global_confirmed = pd.read_csv("./data/global_confirmed.csv")
global_deaths = pd.read_csv("./data/global_confirmed.csv")
global_recovered = pd.read_csv("./data/global_confirmed.csv")

summary_data = pd.read_csv("./data/global_summary.csv")

country_column_key = "Country/Region"
countries = list(summary_data[country_column_key])
