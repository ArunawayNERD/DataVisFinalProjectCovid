from dash.dependencies import Input, Output, State

from app import app


@app.callback(
    Output("main-store", "data"),
    [Input("country-selector", "value")],
    [State("main-store", "data")],
)
def on_country_select_change(country_values, store_data):
    data = store_data if store_data != None else {}
    data["countries"] = country_values if country_values != None else "All"

    return data


# @app.callback(Output("country-test", "children"), [Input("main-store", "data")])
# def on_country_change(store_data):
#     data = store_data if store_data != None else {}

#     return data["countries"] if "countries" in store_data else "All"
