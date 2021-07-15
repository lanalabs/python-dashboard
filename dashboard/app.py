import dash
import yaml
from flask import Flask
import dash_bootstrap_components as dbc

with open("config.yml") as f:
    config = yaml.safe_load(f)

application = Flask("example_dashboard")
app = dash.Dash(name=__name__,
                server=application,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.FLATLY],
                url_base_pathname=f'/{config["dashboard_id"]}/')

server = app.server
