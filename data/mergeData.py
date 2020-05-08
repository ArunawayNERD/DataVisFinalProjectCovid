import pandas as pd

lat_column_key = "Lat"
lon_column_key = "Long"

state_column_key = "Province/State"
country_column_key = "Country/Region"
code_column_key = "Code"

country_to_codes = pd.read_csv("./country_to_codes.csv")


def main():
    mergeCovidData()


def mergeNonCovidData():
    gdp_data_path = ""
    health_spending_path = ""
    pop_density_path = ""


def mergeCovidData():

    global_confirmed = pd.read_csv(
        "./CovidData/time_series_covid19_confirmed_global.csv"
    )
    global_deaths = pd.read_csv("./CovidData/time_series_covid19_deaths_global.csv")
    global_recovered = pd.read_csv(
        "./CovidData/time_series_covid19_recovered_global.csv"
    )

    global_confirmed = get_country_level_data(global_confirmed)
    global_confirmed.to_csv("global_confirmed.csv", index=False)

    global_deaths = get_country_level_data(global_deaths)
    global_deaths.to_csv("global_deaths.csv", index=False)

    global_recovered = get_country_level_data(global_recovered)
    global_recovered.to_csv("global_recovered.csv", index=False)

    latestDataColumn = global_confirmed.columns[-1]

    global_confirmed_latest = global_confirmed[
        [country_column_key, code_column_key, latestDataColumn]
    ]
    global_confirmed_latest = global_confirmed_latest.rename(
        columns={latestDataColumn: "Confirmed"}
    )

    global_deaths_latest = global_deaths[
        [country_column_key, code_column_key, latestDataColumn]
    ]
    global_deaths_latest = global_deaths_latest.rename(
        columns={latestDataColumn: "Deaths"}
    )

    global_recovered_latest = global_recovered[
        [country_column_key, code_column_key, latestDataColumn]
    ]
    global_recovered_latest = global_recovered_latest.rename(
        columns={latestDataColumn: "Recovered"}
    )

    globalSummary = pd.merge(
        global_confirmed_latest,
        global_deaths_latest,
        on=[country_column_key, code_column_key],
        how="left",
    )
    globalSummary = pd.merge(
        globalSummary,
        global_recovered_latest,
        on=[country_column_key, code_column_key],
        how="left",
    )

    globalSummary.to_csv("global_summary.csv", index=False)


def get_country_level_data(dataset):

    return dataset.groupby(country_column_key).apply(aggregate_columns).reset_index()


def aggregate_columns(grouped_data):

    data_columns = list(grouped_data.columns)
    data = {}

    for column in data_columns:
        if column == state_column_key:
            continue
        elif column == country_column_key:

            countryToCodeRow = country_to_codes[
                country_to_codes["COUNTRY"] == grouped_data[column].iloc[0]
            ]

            code = (
                countryToCodeRow.iloc[0]["CODE"] if countryToCodeRow.size > 0 else "N/A"
            )

            data[code_column_key] = code
        elif column == lat_column_key or column == lon_column_key:
            data[column] = grouped_data[column].mean()
        else:
            data[column] = grouped_data[column].sum()

    return pd.Series(data)


if __name__ == "__main__":
    main()
