from dash.dependencies import Input, Output, State
import dash_html_components as html

from app import app

# from components.right_column import render_tab


# def render_tab(selected_tab, store):
#     countries = store["countries"] if store != None and "countries" in store else []

#     return html.Div([html.Div(selected_tab), html.Div(str(countries))])


# @app.callback(
#     Output("right-column-tabs-content", "children"),
#     [Input("right-column-tabs", "value"), Input("main-store", "data")],
# )
# def handle_tab_change(selected_tab, store):
#     return render_tab(selected_tab, store)
