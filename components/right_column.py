import dash_core_components as dcc
import dash_html_components as html

from components.overview_table import overview_table


tabs = ["Totals", "Analyze"]

right_column = html.Div(
    [
        # dcc.Tabs(
        #     id="right-column-tabs",
        #     value=tabs[0],
        #     children=[
        #         dcc.Tab(label=tabs[0], value=tabs[0]),
        #         dcc.Tab(label=tabs[1], value=tabs[1]),
        #     ],
        # ),
        html.Div(
            "GRAPH 1",
            id="right-column-tabs-content",
            style={"disply": "flex", "height": "50%"},
        ),
        html.Div("GRAPH 2", style={"disply": "flex", "height": "50%"},),
    ],
    style={"display": "flex", "flex-direction": "column", "height": "100%",},
)


def render_tab(selected_tab, store):

    countries = store["countries"] if store != None and "countries" in store else []

    if selected_tab == tabs[0]:
        return render_totals_tab(countries)
    else:
        return html.Div([html.Div(selected_tab), html.Div(str(countries))])


def render_totals_tab(countries):
    return overview_table
