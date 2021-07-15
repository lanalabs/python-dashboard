import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px

import pandas as pd

from navbar import navbar


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [10, 10, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

nb = navbar()
layout = html.Div(children=[
    nb,
    html.Center(html.H1(children='Beispiel Seite 2')),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
