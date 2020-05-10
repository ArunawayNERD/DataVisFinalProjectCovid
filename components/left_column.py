import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

from util import get_countries
from data import countries, days


#######
# IDS #
# #####
countries_ids = dict(filter_mode_id="countries-filter-mode", dropdown_id="countries-selector")

covid_data_ids = dict(
    confirmed_button_id="covid-data-confirmed-button",
    deaths_button_id="covid-data-deaths-button",
    recovered_button_id="covid-data-recovered-button",
    scale_id="covid-data-scale",
)

time_range_ids = dict(slider="time_slider_id", selected_text="time_range_display")

graph_options_id = dict(
    graph_one_axis="graph-options-one-axis",
    graph_two_axis="graph-options-two-axis",
    graph_one_switch="graph-options-one-switch",
    graph_two_switch="graph-options-two-switch",
)

store_ids = dict(
    countries_id="countires-store",
    covid_data_id="covid-data-store",
    time_range_id="time-range-store",
    graph_options_id="graph_options_store",
)

countries_data_store_keys = dict(selected_county_codes="selected_county_codes")

covid_data_store_keys = dict(selected_button_id="data_source", selected_scale_value="scale_mode")

time_store_keys = dict(end_date_index="end_date_index")

graph_options_store_keys = dict(
    graph_one_axis="graph_one_axis",
    graph_two_axis="graph_two_axis",
    graph_one_switch="graph_one_switch",
    graph_one_disable="graph_one_disable",
    graph_two_switch="graph_two_switch",
    graph_two_disable="graph_two_disable",
)


scaleOptions = [
    {"label": "Total", "value": "Total"},
    {"label": "Total (Logarithmic)", "value": "TotalLog"},
    {"label": "Per 100K Population", "value": "Per100"},
    {"label": "Percentage of Population", "value": "Percent",},
]

plot_x_axis_options = [
    {"label": "Time", "value": "Time"},
    {"label": "Population", "value": "Pop"},
    {"label": "Population Density", "value": "PopDen"},
    {"label": "Population Percentage 60+", "value": "Pop60"},
]

left_column = html.Div(
    [
        html.Div("Controls", className="controls-header"),
        dcc.Store(id=store_ids["countries_id"]),
        dcc.Store(id=store_ids["covid_data_id"]),
        dcc.Store(id=store_ids["time_range_id"]),
        dcc.Store(id=store_ids["graph_options_id"]),
        html.Div(
            [
                html.Div("Countries", className="controls-group-item controls-group-header"),
                html.Div(
                    children=[
                        html.Div("Subtractive"),
                        daq.ToggleSwitch(id=countries_ids["filter_mode_id"], value=True),
                        html.Div("Additive"),
                    ],
                    className="controls-country-toggle-group controls-group-item",
                ),
                html.Div(
                    dcc.Dropdown(
                        id=countries_ids["dropdown_id"], options=countries, multi=True, style={"width": "100%"},
                    ),
                    className="controls-group-item ",
                ),
            ],
            className="controls-group-container",
        ),
        html.Div(
            [
                html.Div("Covid-19 Data", className="controls-group-item controls-group-header"),
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
                html.Div("Time", className="controls-group-item controls-group-header",),
                html.Div(
                    id=time_range_ids["selected_text"],
                    children="Selected: " + days[0] + " to " + days[-1],
                    className="controls-group-item",
                ),
                html.Div("Update", className="controls-time-slider-label controls-group-item",),
                html.Div(
                    [
                        dcc.Slider(
                            id=time_range_ids["slider"],
                            max=(len(days) - 1),
                            value=(len(days) - 1),
                            step=1,
                            updatemode="drag",
                            className="controls-time-slider",
                        ),
                    ],
                    className="controls-group-item",
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
                    dcc.Dropdown(
                        id=graph_options_id["graph_one_axis"],
                        options=plot_x_axis_options,
                        value="Time",
                        clearable=False,
                        style={"width": "100%"},
                    ),
                    className="controls-group-item",
                ),
                html.Div(
                    daq.BooleanSwitch(
                        id=graph_options_id["graph_one_switch"],
                        on=True,
                        label={"style": {"margin": "0px"}, "label": "Aggregate Country Data"},
                        labelPosition="right",
                        disabled=False,
                    ),
                    className="controls-graphs-toggle controls-group-item",
                ),
                html.Hr(className="controls-group-item"),
                html.Div("Second x-axis", className="controls-group-item"),
                html.Div(
                    dcc.Dropdown(
                        id=graph_options_id["graph_two_axis"],
                        options=plot_x_axis_options,
                        value="Pop",
                        clearable=False,
                        style={"width": "100%"},
                    ),
                    className="controls-group-item",
                ),
                html.Div(
                    daq.BooleanSwitch(
                        id=graph_options_id["graph_two_switch"],
                        on=True,
                        label={"style": {"margin": "0px", "color": "#9E9E9E"}, "label": "Aggregate Country Data"},
                        labelPosition="right",
                        disabled=True,
                        color="#9E9E9E",
                    ),
                    className="controls-group-item",
                ),
            ],
            className="controls-group-container",
        ),
    ],
    className="controls-root",
)
