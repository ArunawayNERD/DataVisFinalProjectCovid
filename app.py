import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from components.left_column import left_column
from components.right_column import right_column
from components.overview_table import overview_table
from components.map import covid_map

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Store(id="main-store"),
        html.Div(children=[html.Div("COVID 19")], className="title"),
        html.Div(children=[left_column], className="left-column"),
        html.Div(children=[right_column], className="right-column"),
        html.Div(children=[covid_map], className="main-graph"),
        html.Div(children=[overview_table], className="second-graph"),
    ],
    className="mainLayout",
)
