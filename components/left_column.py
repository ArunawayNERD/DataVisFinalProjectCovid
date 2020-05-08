import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

from util import get_countries
from data import countries

countryOptions = [{"label": country, "value": country} for country in countries]

left_column = html.Div(
    [
        html.Div("Controls", className="controls-header"),
        html.Div(
            [
                html.Div(
                    "Countries", className="controls-group-item controls-group-header"
                ),
                html.Div(
                    children=[
                        html.Div("Subtractive"),
                        daq.ToggleSwitch(
                            value=True,
                            # label="Behavior",
                            # labelPosition="bottom",
                        ),
                        html.Div("Additive"),
                    ],
                    className="controls-country-toggle-group controls-group-item",
                ),
                html.Div(
                    dcc.Dropdown(
                        id="country-selector",
                        options=countryOptions,
                        multi=True,
                        style={"width": "100%"},
                    ),
                    className="controls-group-item ",
                ),
            ],
            className="controls-group-container",
        ),
        html.Div(
            [
                html.Div(
                    "Covid Data", className="controls-group-item controls-group-header"
                ),
                html.Div(
                    id="country-test",
                    children=[
                        html.Button(
                            "Confirmed",
                            className="controls-button-left controls-button-selected controls-button ",
                        ),
                        html.Button("Deaths", className="controls-button"),
                        html.Button(
                            "Recovered",
                            className="controls-button-right controls-button",
                        ),
                    ],
                    className="controls-group-item",
                ),
                html.Div(
                    [
                        html.Div("Scale", style={"font-size": "bold"}),
                        dcc.RadioItems(
                            options=[
                                {"label": "Total", "value": "Total"},
                                {"label": "Total (Logarithmic)", "value": "TotalLog"},
                                {"label": "Per 100K Population", "value": "Per100"},
                                {
                                    "label": "Percentage of Population",
                                    "value": "Percent",
                                },
                            ],
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
                html.Div(
                    "Time Range", className="controls-group-item controls-group-header",
                ),
                html.Div(
                    html.Div(
                        dcc.Slider(
                            id="slider-updatemode",
                            max=20,
                            value=0,
                            step=1,
                            updatemode="drag",
                            className="controls-time-slider",
                        ),
                        className="controls-group-item",
                    )
                ),
                html.Div(
                    [html.Div("1/22/20"), html.Div("5/1/20")],
                    className="controls-time-labels controls-group-item ",
                ),
            ],
            className="controls-group-container",
        ),
        html.Div(
            [
                html.Div(
                    "Graph Options",
                    className="controls-group-item controls-group-header",
                ),
                html.Div("First x-axis", className="controls-group-item"),
                html.Div(
                    dcc.Dropdown(
                        options=countryOptions, multi=True, style={"width": "100%"},
                    ),
                    className="controls-group-item",
                ),
                html.Div("Second x-axis", className="controls-group-item"),
                html.Div(
                    dcc.Dropdown(
                        options=countryOptions, multi=True, style={"width": "100%"},
                    ),
                    className="controls-group-item",
                ),
                # html.Div(
                #     dcc.Dropdown(
                #         options=countryOptions, multi=True, style={"width": "100%"},
                #     ),
                #     className="controls-group-item ",
                # ),
            ],
            className="controls-group-container",
        ),
    ],
    className="controls-root",
)
