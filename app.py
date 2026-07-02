import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# load your output file
df = pd.read_csv("output.csv")

# convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# sort by date
df = df.sort_values("date")

# create line chart
fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time")

# create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser"),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
   app.run(debug=True)