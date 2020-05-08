import dash
import dash_core_components as dcc
import plotly.graph_objects as go

from data import summary_data

map_figure = go.Figure(
    data=go.Choropleth(
        locations=summary_data["Code"],
        z=summary_data["Confirmed"],
        text=summary_data["Country/Region"],
        # colorscale="jet",
        reversescale=True,
    ),
    layout=go.Layout(
        margin=dict(t=0, b=0, l=16, r=0),
        autosize=True,
        geo=dict(showcountries=True),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    ),
)
# map_figure.update_traces(showscale=False)


covid_map = dcc.Graph(figure=map_figure, style={"height": "100%"})
