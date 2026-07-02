import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

app.layout = html.Div(style={"fontFamily": "Arial", "padding": "20px"}, children=[

    html.H1("Soul Foods Sales Visualiser", style={"textAlign": "center"}),

    html.H3("Filter by Region"),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        labelStyle={"display": "inline-block", "marginRight": "15px"}
    ),

    dcc.Graph(id="line-chart")
])

# Callback to update graph
@app.callback(
    Output("line-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales ({selected_region})"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)