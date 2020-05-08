import dash_table
from data import summary_data


overview_table = dash_table.DataTable(
    id="overview-table",
    columns=[{"name": i, "id": i} for i in summary_data.columns],
    data=summary_data.to_dict("records"),
    page_size=5,
    style_table={"height": "100%"},
)
