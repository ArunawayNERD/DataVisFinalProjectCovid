import pandas as pd
import math

global_confirmed = pd.read_csv("./data/global_confirmed.csv")
global_deaths = pd.read_csv("./data/global_confirmed.csv")
global_recovered = pd.read_csv("./data/global_confirmed.csv")

summary_data = pd.read_csv("./data/global_summary.csv")

country_name_column_key = "Country/Region"
country_code_column_key = "Code"

countries = [
    {"label": row[0], "value": row[1]}
    for row in summary_data[[country_name_column_key, country_code_column_key]].values
    if isinstance(row[1], str)  # if its not than we didn't have the code because pandas is reading 'N/A' as nan
]

days = list(global_confirmed.columns[2:])
