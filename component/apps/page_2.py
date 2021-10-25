from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash

import dash_highchart
import plotly.express as px

from functools import lru_cache
import pandas as pd
import lana_listener

from navbar import navbar
from app import app
from dashboard_components.indicator_objects import indicator_div
from dashboard_components.tables import generate_dash_table
from dashboard_components.logs import get_log_activities
from dashboard_components.kpis import activity_per_timeUnit
from dashboard_components.formatting import remove_bar_config


global_df = pd.DataFrame()

ll = lana_listener.LanaListener(
    id='LanaListener',
    lana_api_key='684aeb64097741bfa66a20712e36a11e',
    lana_log_id='70d5b7ae-42d2-4196-9a26-a313d3d717ff',
    lana_trace_filter_sequence='[]'
)

layout = html.Div(children=[
    ll,
    dbc.Row([dbc.Col(html.Div(id="cost_table_div"), width={"size": 5, "offset": 1}),
             dbc.Col(id="hc-bar-chart", width=4)])
])


lru_cache(maxsize=5)
def create_activity_df(log_id, api_key, tfs):
    global_df = get_log_activities(log_id, api_key, tfs)
    global_df.columns = ["Häufigkeit", "Aktivitätsname", "medianDuration"]
    global_df["Kosten"] = 0
    global_df["Gesamtkosten"] = 0
    global_df = global_df[["Aktivitätsname", "Häufigkeit", "Kosten", "Gesamtkosten"]]
    return global_df


@app.callback(
    Output("cost_table_div", "children"),
    [Input('LanaListener', 'lana_api_key'),
     Input('LanaListener', 'lana_log_id'),
     Input('LanaListener', 'lana_trace_filter_sequence')])
def gen_table(api_key, log_id, tfs):
    global_df = create_activity_df(log_id, api_key, tfs)
    return [generate_dash_table(global_df,
                                id="cost_table",
                                sorting=[{"column_id": 'Häufigkeit',
                                          "direction": "desc"}],
                                dropdowns={"Aktivitätsname": global_df["Aktivitätsname"].unique()},
                                num_elements=10)]


@app.callback(
    Output('cost_table', 'data'),
    Input('cost_table', 'data_timestamp'),
    State('cost_table', 'data'),
    State('cost_table', 'columns'),
    State('LanaListener', 'lana_api_key'),
    State('LanaListener', 'lana_log_id'),
    State('LanaListener', 'lana_trace_filter_sequence'))
def update_table_data(n_clicks, timestamp, rows, columns, api_key, log_id, tfs): # noqa
    ctx = dash.callback_context
    if not ctx.triggered:
        changed_object = None
    else:
        changed_object = ctx.triggered[0]['prop_id'].split('.')[0]

    global_df = create_activity_df(log_id, api_key, tfs)

    if changed_object is None:
        return rows

    if changed_object == "new_row_activity_table":
        rows.append({c['id']: '' for c in columns})
        return rows

    if changed_object == "cost_table":
        for row in rows:
            try:
                row["Häufigkeit"] = global_df[global_df["Aktivitätsname"] == row["Aktivitätsname"]]["Häufigkeit"].values[0]
                if row["Kosten"] == "":
                    row["Kosten"] = 0
            except Exception:
                pass
            try:
                row['Gesamtkosten'] = int(row['Häufigkeit']) * int(row["Kosten"])
            except Exception:
                row['Gesamtkosten'] = 'NA'
        return rows

@app.callback(
    Output("activity_p_month", "figure"),
    Input('cost_table', 'active_cell'),
    State('cost_table', 'data'),
    State('LanaListener', 'lana_api_key'),
    State('LanaListener', 'lana_log_id'),
    State('LanaListener', 'lana_trace_filter_sequence')
)
def update_frequency_graph(cell, data, api_key, log_id, tfs):
    row = cell["row"]
    res = data[row]["Aktivitätsname"]
    df = activity_per_timeUnit(api_key=api_key, log_id=log_id, tfs=tfs,
                               activities=[res], frequency="byMonth")
    df["byMonth_dt"] = pd.to_datetime(df.byMonth)
    fig = px.bar(df, x='byMonth_dt', y='frequency',
                 title=f"Häufigkeit pro Monat: {res}",
                       labels={'byMonth_dt': 'Monat'},
                       template="ggplot2")
    return fig

@app.callback(
    Output("hc-bar-chart", "children"),
    Input('cost_table', 'active_cell'),
    State('cost_table', 'data'),
    State('LanaListener', 'lana_api_key'),
    State('LanaListener', 'lana_log_id'),
    State('LanaListener', 'lana_trace_filter_sequence')
)
def update_hc_frequency_graph(cell, data, api_key, log_id, tfs):
    row = cell["row"]
    res = data[row]["Aktivitätsname"]
    df = activity_per_timeUnit(api_key=api_key, log_id=log_id, tfs=tfs,
                               activities=[res], frequency="byMonth")
    df["byMonth_dt"] = pd.to_datetime(df.byMonth)
    
    return dash_highchart.DashHighchart(
            id='hc-bar-chart-fig',
            chartOptions={
                'chart': {
                    'type': 'bar'
                },
                'xAxis': {
                    'categories': df["byMonth"],
                },
                'title': {
                    'text': f'Frequency per Month: {res}'
                },
                'series': [
                    {'data': df["frequency"]}
                ],
                'colors': ["#008580", "#c4345d", "#6baed6", "#9ecae1",
                        "#c6dbef", "#e6550d", "#fd8d3c", "#fdae6b"],
                'plotOptions': {}
            }
        )


@app.callback(
    Output('total_costs', 'children'),
    Input('cost_table', 'data_timestamp'),
    State('cost_table', 'data'),
    State('cost_table', 'columns'))
def update_indicator_col(timestamp, rows, columns):
    total_cost = 0
    for row in rows:
        try:
            total_cost += int(row['Häufigkeit']) * int(row["Kosten"])
        except Exception:
            pass
    ind = indicator_div(total_cost, title="Summe Gesamtkosten")
    return ind
