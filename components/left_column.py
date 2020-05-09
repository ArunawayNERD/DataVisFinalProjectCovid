import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

from util import get_countries
from data import countries, days


#######
# IDS #
# #####
covid_data_ids = dict(
    confirmed_button_id="covid-data-confirmed-button",
    deaths_button_id="covid-data-deaths-button",
    recovered_button_id="covid-data-recovered-button",
    scale_id="covid-data-scale",
)

store_ids = dict(covid_data_filters_id="covid-data-store",)

covid_data_store_keys = dict(selected_button_id="data_source", selected_scale_value="scale_mode")


countryOptions = [{"label": country, "value": country} for country in countries]
scaleOptions = [
    {"label": "Total", "value": "Total"},
    {"label": "Total (Logarithmic)", "value": "TotalLog"},
    {"label": "Per 100K Population", "value": "Per100"},
    {"label": "Percentage of Population", "value": "Percent",},
]

left_column = html.Div(
    [
        html.Div("Controls", className="controls-header"),
        dcc.Store(id="countires-selected-store"),
        html.Div(
            [
                html.Div("Countries", className="controls-group-item controls-group-header"),
                html.Div(
                    children=[
                        html.Div("Subtractive"),
                        daq.ToggleSwitch(id="countries-filter-mode", value=True),
                        html.Div("Additive"),
                    ],
                    className="controls-country-toggle-group controls-group-item",
                ),
                html.Div(
                    dcc.Dropdown(id="countries-selector", options=countryOptions, multi=True, style={"width": "100%"},),
                    className="controls-group-item ",
                ),
            ],
            className="controls-group-container",
        ),
        html.Div(
            [
                html.Div("Covid-19 Data", className="controls-group-item controls-group-header"),
                dcc.Store(id=store_ids["covid_data_filters_id"]),
                html.Div(
                    children=[
                        html.Button(
                            id=covid_data_ids["confirmed_button_id"],
                            children="Confirmed",
                            className="controls-button-left controls-button-selected controls-button ",
                        ),
                        html.Button(
                            id=covid_data_ids["deaths_button_id"], children="Deaths", className="controls-button",
                        ),
                        html.Button(
                            id=covid_data_ids["recovered_button_id"],
                            children="Recovered",
                            className="controls-button-right controls-button",
                        ),
                    ],
                    className="controls-group-item",
                ),
                html.Div(
                    [
                        html.Div("Scale", style={"font-weight": "bold"}),
                        dcc.RadioItems(
                            id=covid_data_ids["scale_id"],
                            options=scaleOptions,
                            value="Total",
                            className="controls-scale-type-options",
                        ),
                    ],
                    className="controls-scale-type-group controls-group-item ",
                ),
            ],
            className="controls-group-container",
        ),
        html.Div(
            [
                html.Div("Time Range", className="controls-group-item controls-group-header",),
                html.Div(
                    html.Div(
                        dcc.Slider(
                            id="time-range-slider",
                            max=(len(days) - 1),
                            value=(len(days) - 1),
                            step=1,
                            updatemode="drag",
                            className="controls-time-slider",
                        ),
                        className="controls-group-item",
                    )
                ),
                html.Div(
                    [html.Div(days[0]), html.Div(days[-1])], className="controls-time-labels controls-group-item ",
                ),
            ],
            className="controls-group-container",
        ),
        html.Div(
            [
                html.Div("Graph Options", className="controls-group-item controls-group-header",),
                html.Div("First x-axis", className="controls-group-item"),
                html.Div(
                    dcc.Dropdown(id="first-graph-axis", options=countryOptions, multi=True, style={"width": "100%"},),
                    className="controls-group-item",
                ),
                html.Div("Second x-axis", className="controls-group-item"),
                html.Div(
                    dcc.Dropdown(id="second-graph-axis", options=countryOptions, multi=True, style={"width": "100%"},),
                    className="controls-group-item",
                ),
            ],
            className="controls-group-container",
        ),
    ],
    className="controls-root",
)
