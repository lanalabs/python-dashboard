import dash
import os
from flask import Flask
from urllib.parse import urlparse
import dash_bootstrap_components as dbc

# The hardcoded part can be removed once the JANUS_URL can be read from the environment.
# At the current stage it is not present.
try:
    fooConfig = urlparse(os.environ['JANUS_URL'])
    config = {"scheme": fooConfig.scheme,
              "host": fooConfig.hostname,
              "port": fooConfig.port}
except Exception:
    config = {"scheme": "https",
              "host": "cloud-backend.lanalabs.com",
              "port": 4000}

config["dashboard_id"] = os.path.basename(os.getcwd())
print(config)

application = Flask("example_dashboard")
app = dash.Dash(name=__name__,
                server=application,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.FLATLY],
                url_base_pathname=f'/{config["dashboard_id"]}/')

server = app.server
