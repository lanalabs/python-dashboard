from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, application, config
from apps import page_1, page_2


app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

dashboard_id = config["dashboard_id"]


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == f'/{dashboard_id}/apps/app1':
        return page_1.layout
    elif pathname == f'/{dashboard_id}/apps/app2':
        return page_2.layout
    else:
        return page_1.layout


if __name__ == '__main__':
    app.run_server(debug=True)
