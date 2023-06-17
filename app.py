# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html

df = pd.read_csv("perte-de-couverture-forestiere-et-emissions-de-co2-de-2001-a-2020.csv")

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(children="Perte de couverture forestière et émission de CO2 en CIV 🇨🇮", style={"textAlign": "center"}),
        dcc.Dropdown(df.Catégorie.unique(), "Perte de couvert forestier arboré (ha)", id="dropdown-selection"),
        dcc.Graph(id="graph-content"),
    ]
)


@callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    dff = df[df.Catégorie == value]
    return px.line(dff, x="Année", y="Valeur")


if __name__ == "__main__":
    app.run_server(debug=True)
