import dash
import dash_core_components as dcc
import dash_html_components as html

from util import get_countries


def get_left_column(covid_data):

    countryOptions = [{'label': country, 'value': country}
                      for country in get_countries(covid_data)]

    return html.Div([
        html.Div("Controls", className='controls-header'),
        dcc.Dropdown(id='country-selector',
                     options=countryOptions,  multi=True),
        html.Div(id='country-test', children='init')
    ], className='controls-root')
