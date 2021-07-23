from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc


import pylana
import lana_listener
import json
import os

from urllib.parse import urlparse
from navbar import navbar
from graph_objects import indicator_div, indicator_col
from app import app

ll = lana_listener.LanaListener(
    id='LanaListener',
    lana_api_key='',
    lana_log_id='',
    lana_trace_filter_sequence='[]'
)

nb = navbar()


ind1 = indicator_col(21000, title="Statischer Indicator", width=3)

layout = html.Div(children=[ll,
                            nb,
                            html.Center(
                                html.H1(children='Übersicht der Logs')),
                            html.Br(),
                            dbc.Row([ind1,
                                     dbc.Col(
                                         id="median_duration_with_tfs",
                                         width={"size": 3}),
                                     dbc.Col(id="number_cases",
                                             width={"size": 3}),
                                     dbc.Col(id="number_cases_tfs",
                                             width={"size": 3})
                                     ]),
                            html.Div(id='my-output_page1')])


@app.callback(
    Output(component_id='median_duration_with_tfs',
           component_property='children'),
    [Input('LanaListener', 'lana_api_key'),
     Input('LanaListener', 'lana_log_id'),
     Input('LanaListener', 'lana_trace_filter_sequence')]
)
def update_indicator_median_tfs(api_key, log_id, tfs):
    fooConfig = urlparse(os.environ['JANUS_URL'])
    api_key = api_key[8:]
    tfs = json.loads(tfs)
    api = pylana.create_api(**{
        "scheme": fooConfig.scheme,
        "host": fooConfig.hostname,
        "port": fooConfig.port,
        "token": api_key
    })

    df = api.aggregate(log_id, metric="duration",
                       aggregation_function="median",
                       trace_filter_sequence=tfs)
    val = df["duration"].values[0] / (60 * 60 * 24 * 1000)  # Days

    ind = indicator_div(val, title="Mediane Durchlaufzeit in Tagen (mit TFS)")
    return ind


@app.callback(
    Output(component_id='number_cases', component_property='children'),
    [Input('LanaListener', 'lana_api_key'),
     Input('LanaListener', 'lana_log_id')]
)
def number_cases(api_key, log_id):
    fooConfig = urlparse(os.environ['JANUS_URL'])
    api_key = api_key[8:]
    api = pylana.create_api(**{
        "scheme": fooConfig.scheme,
        "host": fooConfig.hostname,
        "port": fooConfig.port,
        "token": api_key
    })

    df = api.aggregate(log_id, metric="frequency", aggregation_function="sum")
    val = df["frequency"].values[0]

    ind = indicator_div(val, title="Anzahl Cases (ohne TFS)")
    return ind


@app.callback(
    Output(component_id='number_cases_tfs', component_property='children'),
    [Input('LanaListener', 'lana_api_key'),
     Input('LanaListener', 'lana_log_id'),
     Input('LanaListener', 'lana_trace_filter_sequence')]
)
def number_case_tfs(api_key, log_id, tfs):
    fooConfig = urlparse(os.environ['JANUS_URL'])
    api_key = api_key[8:]
    tfs = json.loads(tfs)

    api = pylana.create_api(**{
        "scheme": fooConfig.scheme,
        "host": fooConfig.hostname,
        "port": fooConfig.port,
        "token": api_key
    })

    df = api.aggregate(log_id, metric="frequency",
                       aggregation_function="sum", trace_filter_sequence=tfs)
    val = df["frequency"].values[0]

    ind = indicator_div(val, title="Anzahl Cases (mit TFS)")
    return ind


@app.callback(
    Output(component_id='my-output_page1', component_property='children'),
    [Input('LanaListener', 'lana_api_key'),
     Input('LanaListener', 'lana_log_id'),
     Input('LanaListener', 'lana_trace_filter_sequence')]
)
def update_output_div_abc(v1, v2, v3):
    return 'Api Key: {}, Log id: {}, TFS: {}'.format(v1, v2, v3)
