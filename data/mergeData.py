import pandas as pd

lat_column_key = "Lat"
lon_column_key = "Long"

state_column_key = "Province/State"
country_column_key = "Country/Region"
code_column_key = "Code"

country_to_codes = pd.read_csv("./country_to_codes.csv")

region_codes_to_skip = [
    1,
    2,
    15,
    202,
    14,
    17,
    18,
    11,
    19,
    21,
    419,
    29,
    13,
    5,
    142,
    143,
    30,
    62,
    35,
    34,
    145,
    150,
    151,
    154,
    39,
    155,
    9,
    53,
    54,
    57,
    61,
    344,
    446,
    530,
    275,
    736,
    836,
]


def main():
    mergeCovidData()
    mergeNonCovidData()


def mergeNonCovidData():
    gdp_data = pd.read_csv("./raw_data/SYB62_230_201904_GDP and GDP Per Capita.csv", skiprows=1, engine="python")
    gdp_data = prep_drop_extra_data(gdp_data)

    import_export_data = pd.read_csv(
        "./raw_data/SYB62_123_201907_Total Imports, Exports and Balance of Trade.csv", skiprows=1, engine="python"
    )
    import_export_data = prep_drop_extra_data(import_export_data)

    health_spending_data = pd.read_csv(
        "./raw_data/SYB63_325_202003_Expenditure on Health.csv", skiprows=1, engine="python"
    )

    health_spending_data = prep_drop_extra_data(health_spending_data)

    # population, population density and pop over 60
    pop_density_data = pd.read_csv(
        "./raw_data/SYB62_1_201907_Population, Surface Area and Density.csv", skiprows=1, engine="python"
    )
    latest_year = 2019

    pop_density_data = prep_drop_extra_data(pop_density_data)

    total_popultion = pop_density_data[
        (pop_density_data["Year"] == latest_year)
        & (pop_density_data["Series"] == "Population mid-year estimates (millions)")
    ]
    total_popultion = total_popultion[[country_column_key, code_column_key, "Value"]]
    total_popultion = total_popultion.rename(columns={"Value": "Population (Millions)"})

    print(total_popultion.head())

    density = pop_density_data[
        (pop_density_data["Year"] == latest_year) & (pop_density_data["Series"] == "Population density")
    ]
    density = density[[country_column_key, code_column_key, "Value"]]
    density = density.rename(columns={"Value": "Population Density"})

    pop_over_60 = pop_density_data[
        (pop_density_data["Year"] == latest_year)
        & (pop_density_data["Series"] == "Population aged 60+ years old (percentage)")
    ]
    pop_over_60 = pop_over_60[[country_column_key, code_column_key, "Value"]]
    pop_over_60 = pop_over_60.rename(columns={"Value": "Population Percentage Over 60"})

    pop_data_out = pop_density_data[[country_column_key, code_column_key]].drop_duplicates(ignore_index=True)

    pop_data_out = pd.merge(pop_data_out, total_popultion, on=[country_column_key, code_column_key], how="left")
    pop_data_out = pd.merge(pop_data_out, density, on=[country_column_key, code_column_key], how="left")
    pop_data_out = pd.merge(pop_data_out, pop_over_60, on=[country_column_key, code_column_key], how="left")

    pop_data_out.to_csv("./population_data.csv")


def prep_drop_extra_data(data):
    preped_data = data.rename(columns={"Unnamed: 1": country_column_key})
    preped_data = preped_data[~preped_data["Region/Country/Area"].isin(region_codes_to_skip)]
    preped_data = preped_data.assign(
        Code=preped_data[country_column_key].apply(lambda country: country_name_to_code(country))
    )

    return preped_data.drop(columns=["Footnotes", "Source", "Region/Country/Area"])


def mergeCovidData():

    global_confirmed = pd.read_csv("./raw_data/time_series_covid19_confirmed_global.csv")
    global_deaths = pd.read_csv("./raw_data/time_series_covid19_deaths_global.csv")
    global_recovered = pd.read_csv("./raw_data/time_series_covid19_recovered_global.csv")

    global_confirmed = get_country_level_data(global_confirmed)
    global_confirmed.to_csv("global_confirmed.csv", index=False)

    global_deaths = get_country_level_data(global_deaths)
    global_deaths.to_csv("global_deaths.csv", index=False)

    global_recovered = get_country_level_data(global_recovered)
    global_recovered.to_csv("global_recovered.csv", index=False)

    # latestDataColumn = global_confirmed.columns[-1]

    # global_confirmed_latest = global_confirmed[[country_column_key, code_column_key, latestDataColumn]]
    # global_confirmed_latest = global_confirmed_latest.rename(columns={latestDataColumn: "Confirmed"})

    # global_deaths_latest = global_deaths[[country_column_key, code_column_key, latestDataColumn]]
    # global_deaths_latest = global_deaths_latest.rename(columns={latestDataColumn: "Deaths"})

    # global_recovered_latest = global_recovered[[country_column_key, code_column_key, latestDataColumn]]
    # global_recovered_latest = global_recovered_latest.rename(columns={latestDataColumn: "Recovered"})

    # globalSummary = pd.merge(
    #     global_confirmed_latest, global_deaths_latest, on=[country_column_key, code_column_key], how="left"
    # )
    # globalSummary = pd.merge(
    #     globalSummary, global_recovered_latest, on=[country_column_key, code_column_key], how="left",
    # )

    # globalSummary.to_csv("global_summary.csv", index=False)


def get_country_level_data(dataset):

    preped_data = dataset.replace(to_replace="US", value="United States of America")

    return preped_data.groupby(country_column_key).apply(aggregate_columns).reset_index()


def aggregate_columns(grouped_data):

    data_columns = list(grouped_data.columns)
    data = {}

    for column in data_columns:
        if column == state_column_key or column == lat_column_key or column == lon_column_key:
            continue
        elif column == country_column_key:

            country = grouped_data[column].iloc[0]

            # countryToCodeRow = country_to_codes[country_to_codes["COUNTRY"] == grouped_data[column].iloc[0]]

            # code = countryToCodeRow.iloc[0]["CODE"] if countryToCodeRow.size > 0 else "N/A"

            data[code_column_key] = country_name_to_code(country)
        else:
            data[column] = grouped_data[column].sum()

    return pd.Series(data)


def country_name_to_code(country):
    countryToCodeRow = country_to_codes[country_to_codes["COUNTRY"] == country]

    code = countryToCodeRow.iloc[0]["CODE"] if countryToCodeRow.size > 0 else "N/A"
    return code


if __name__ == "__main__":
    main()
