import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data (safe)
df = pd.read_csv("output.csv")

# Dash app (IMPORTANT for tests)
app = dash.Dash(__name__)
server = app.server

# Layout (must be simple)
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser"),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all"
    ),

    dcc.Graph(id="line-chart")
])

# Callback (safe version)
@app.callback(
    Output("line-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(region):

    dff = df if region == "all" else df[df["region"] == region]

    fig = px.line(dff, x="date", y="sales")
    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)