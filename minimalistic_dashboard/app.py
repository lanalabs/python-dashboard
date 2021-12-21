import dash
import os
import dash_bootstrap_components as dbc

from flask import Flask
from urllib.parse import urlparse

try:
    fooConfig = urlparse(os.environ['JANUS_URL'])
    config = {"scheme": fooConfig.scheme,
              "host": fooConfig.hostname,
              "port": fooConfig.port,
              "url": fooConfig.url,
              "dashboard_id": os.path.basename(os.getcwd())}
except Exception:
    config = {"scheme": "http",
              "host": "janus",
              "port": 4000,
              "url": "http://localhost",
              "dashboard_id": os.path.basename(os.getcwd())}

application = Flask("example_dashboard")

app = dash.Dash(name=__name__,
                server=application,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.FLATLY],
                url_base_pathname=f'/{config["dashboard_id"]}/')

server = app.server
