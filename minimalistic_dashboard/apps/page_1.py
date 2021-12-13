import lana_listener
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app
from api_calls import number_of_cases
from dash.dependencies import Input, Output
from dashboard_components.indicator_objects import indicator_div

llistener = lana_listener.LanaListener(
    id='LanaListener',
    lana_api_key='',
    lana_log_id='',
    lana_trace_filter_sequence='[]'
)

layout = html.Div(children=[llistener,
                            html.Br(),
                            dbc.Row([dbc.Col(id="number_cases", width={"size": 3}),
                                     dbc.Col(id="number_cases_tfs", width={"size": 3})
                                     ])])

@app.callback(
    Output(component_id='number_cases', component_property='children'),
    [Input('LanaListener', 'lana_api_key'),
     Input('LanaListener', 'lana_log_id')]
)
def number_cases(api_key, log_id):
    num_cases = number_of_cases(log_id, api_key)
    ind = indicator_div(num_cases, title="Anzahl Cases (ohne TFS)")
    return ind

@app.callback(
    Output(component_id='number_cases_tfs', component_property='children'),
    [Input('LanaListener', 'lana_api_key'),
     Input('LanaListener', 'lana_log_id'),
     Input('LanaListener', 'lana_trace_filter_sequence')]
)
def number_case_tfs(api_key, log_id, tfs):
    num_cases = number_of_cases(log_id, api_key, tfs)
    ind = indicator_div(num_cases, title="Anzahl Cases (mit TFS)")
    return ind
