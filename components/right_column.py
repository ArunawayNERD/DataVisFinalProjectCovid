import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import plotly.graph_objects as go

from data import country_name_column_key, country_code_column_key, global_confirmed, days


def produce_line_graph(data, countries):
    # switch between data set they selected

    lineGraph = go.Figure()

    # for each country selected
    country_data = data.loc[data["Code"] == "USA", :].values[0][2:]

    lineGraph.add_trace(go.Scatter(x=days, y=country_data))

    return lineGraph


# switch between data set they selected

graphOneLine = produce_line_graph(global_confirmed, [])
graphTwoLine = produce_line_graph(global_confirmed, [])

# for each country selected


right_column = html.Div(
    [
        html.Div(
            dcc.Graph(figure=graphOneLine), id="right-column-tabs-content", style={"disply": "flex", "margin": "16px"},
        ),
        html.Div(dcc.Graph(figure=graphTwoLine), style={"disply": "flex", "margin": "16px"},),
    ],
    style={"display": "flex", "flex-direction": "column", "height": "100%",},
)
