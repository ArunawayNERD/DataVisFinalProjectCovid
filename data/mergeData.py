import pandas as pd

lat_column_key = 'Lat'
lon_column_key = 'Long'

state_column_key = 'Province/State'
country_column_key = 'Country/Region'


def main():
    mergeCovidData()


def mergeNonCovidData():
    gdp_data_path = ''
    health_spending_path = ''
    pop_density_path


def mergeCovidData():
    global_confirmed_path = './CovidData/time_series_covid19_confirmed_global.csv'
    global_deaths_path = './CovidData/time_series_covid19_deaths_global.csv'
    global_recovered_path = './CovidData/time_series_covid19_recovered_global.csv'

    global_confirmed = pd.read_csv(global_confirmed_path)
    global_deaths = pd.read_csv(global_deaths_path)
    global_recovered = pd.read_csv(global_recovered_path)

    global_confirmed = get_country_level_data(
        global_confirmed).to_csv('confirmed_global.csv', index=False)

    global_deaths = get_country_level_data(global_deaths).to_csv(
        'confirmed_deaths.csv', index=False)

    global_recovered = get_country_level_data(global_recovered).to_csv(
        'confirmed_recovered.csv', index=False)


def get_country_level_data(dataset):

    return dataset.groupby(country_column_key).apply(aggregate_columns).reset_index()


def aggregate_columns(grouped_data):

    data_columns = list(grouped_data.columns)
    data = {}

    for column in data_columns:
        if column == state_column_key or column == country_column_key:
            continue
        elif column == lat_column_key or column == lon_column_key:
            data[column] = grouped_data[column].mean()
        else:
            data[column] = grouped_data[column].sum()

    return pd.Series(data)


if __name__ == "__main__":
    main()
