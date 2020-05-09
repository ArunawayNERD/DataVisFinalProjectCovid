
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app

from data import countries, days
from components.left_column import store_ids, countries_ids, covid_data_ids, time_range_ids, countries_data_store_keys, covid_data_store_keys, time_store_keys


######################
# Countries controls #
######################

@app.callback(
    Output(store_ids['countries_id'], 'data'), 
    [Input(countries_ids['filter_mode_id'], 'value'),
     Input(countries_ids['dropdown_id'], 'value'),],
)
def store_selected_countries(is_filter_additive, selected_country_codes):
    selected_codes = []

    if is_filter_additive:
        selected_codes = selected_country_codes
    else:
        selected_codes = [ country['value'] for country in countries if country['value'] not in selected_country_codes]

    store_data = {countries_data_store_keys['selected_county_codes']:selected_codes}

    return store_data


#######################
# Covid data controls #
#######################
@app.callback(
    Output(store_ids['covid_data_id'], 'data'), 
    [Input(covid_data_ids['confirmed_button_id'], 'n_clicks'),
     Input(covid_data_ids['deaths_button_id'], 'n_clicks'),
     Input(covid_data_ids['recovered_button_id'], 'n_clicks'), 
     Input(covid_data_ids['scale_id'], 'value')],
    [State(store_ids['covid_data_id'], 'data')]
)
def store_covid_data_control_selection(confirmed, deaths, recovered, scale_value, store):
    context = dash.callback_context
    selected_id = ""
    
    if not context.triggered:
        raise PreventUpdate
    else:
        selected_id = context.triggered[0]['prop_id'].split('.')[0]


    stored_data = store if store != None else {}

    if selected_id==covid_data_ids['scale_id']:
        stored_data[covid_data_store_keys['selected_scale_value']] = scale_value
    else:
        stored_data[covid_data_store_keys['selected_button_id']] = selected_id 

    return stored_data

@app.callback(
    [Output(covid_data_ids['confirmed_button_id'], 'className'),
     Output(covid_data_ids['deaths_button_id'], 'className'),
     Output(covid_data_ids['recovered_button_id'], 'className')], 
    [Input(store_ids['covid_data_id'], 'data')]
)
def update_clicked_button_style(store):

    if store == None or covid_data_store_keys['selected_button_id'] not in store:
        raise PreventUpdate

    selected_id = store[covid_data_store_keys['selected_button_id']]
    
    confirmed_className = 'controls-button-left controls-button'
    deaths_className = 'controls-button'
    recovered_className = "controls-button-right controls-button"

    if selected_id == covid_data_ids['confirmed_button_id']:
        confirmed_className = "controls-button-selected " + confirmed_className
    elif selected_id == covid_data_ids['deaths_button_id']:
        deaths_className = "controls-button-selected " + deaths_className
    else:
        recovered_className = "controls-button-selected " + recovered_className

    return confirmed_className, deaths_className, recovered_className


#######################
# Time Range controls #
#######################

@app.callback(
    Output(store_ids['time_range_id'], 'data'),
    [Input(time_range_ids['slider'], 'value')]
)
def store_time_range(selected_index):
    return {time_store_keys['end_date_index']: selected_index}

@app.callback(
    Output(time_range_ids['selected_text'], 'children'),
    [Input(store_ids['time_range_id'], 'data')]
)
def update_slider_tooltip(store):
    selected_index = 0
    
    if store == None or time_store_keys['end_date_index'] not in store:
        raise PreventUpdate
    else:
        selected_index = store[time_store_keys['end_date_index']]

    selected_day = days[selected_index]

    return "Selected: " + days[0] + " to " + selected_day,


