import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from components import left_column


covid_data = pd.read_csv('./data/confirmed_global.csv')


app = dash.Dash(__name__)


app.layout = html.Div(children=[
    dcc.Store(id="main-store"),
    html.Div(children=['COVID 19'], className='title'),
    html.Div(children=[left_column.get_left_column(
        covid_data)], className='left-column'),
    html.Div(children=['right column'], className='right-column'),
    html.Div(children=['main-graph'], className='main-graph'),
    html.Div(children=['second-graph'], className='second-graph'),
],
    className='mainLayout'
)
