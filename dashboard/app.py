import dash
import yaml
from flask import Flask
import dash_bootstrap_components as dbc
import os

# TODO, begin: this should not exists.
with open("config.yml") as f:
    config = yaml.safe_load(f)

print(config)
# TODO, end.

dashboard_id = os.path.basename(os.getcwd())

application = Flask("example_dashboard")
app = dash.Dash(name=__name__,
                server=application,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.FLATLY],
                url_base_pathname=f'/{dashboard_id}/')

server = app.server
