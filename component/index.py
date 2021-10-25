from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, application, config
from apps import page_1, page_2


print(f"Server {str(application)} running.")


app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

dashboard_id = config["dashboard_id"]


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return page_2.layout

if __name__ == '__main__':
    app.run_server(debug=True)
