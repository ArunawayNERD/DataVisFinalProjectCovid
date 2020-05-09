
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app

from components.left_column import store_ids, covid_data_ids, covid_data_store_keys

@app.callback(
    [Output(covid_data_ids['confirmed_button_id'], 'className'),
     Output(covid_data_ids['deaths_button_id'], 'className'),
     Output(covid_data_ids['recovered_button_id'], 'className')], 
    [Input(store_ids['covid_data_filters_id'], 'data')]
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

@app.callback(
    Output(store_ids['covid_data_filters_id'], 'data'), 
    [Input(covid_data_ids['confirmed_button_id'], 'n_clicks'),
     Input(covid_data_ids['deaths_button_id'], 'n_clicks'),
     Input(covid_data_ids['recovered_button_id'], 'n_clicks'), 
     Input(covid_data_ids['scale_id'], 'value')],
    [State(store_ids['covid_data_filters_id'], 'data')]
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








