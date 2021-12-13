import dash_core_components as dcc
import dash_html_components as html

from app import app, application, config
from apps import page_1
from dash.dependencies import Input, Output

print(f"Server {str(application)} running.")

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    dashboard_id = config["dashboard_id"]
    if pathname == f'/{dashboard_id}/apps/app1':
        return page_1.layout
    else:
        return page_1.layout

if __name__ == '__main__':
    app.run_server(debug=False)
