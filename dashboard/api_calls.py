import pylana
import json
from app import config


def create_connection(api_key, port=None):
    scheme = config["scheme"]
    host = config["host"]

    if api_key[:3] == "API":
        api_key = api_key[8:]
    if scheme != "https":
        port = port if port else 4000
        api = pylana.create_api(**{
            "scheme": scheme,
            "host": host,
            "port": port,
            "token": api_key
        })
        return api
    else:
        api = pylana.create_api(**{
            "scheme": scheme,
            "host": host,
            "token": api_key
        })
        return api


def aggregate(api_key, trace_filter_sequence, **kwargs):
    trace_filter_sequence = json.loads(trace_filter_sequence) if trace_filter_sequence else []

    api = create_connection(api_key)
    df = api.aggregate(trace_filter_sequence=trace_filter_sequence, **kwargs)
    return df

def number_of_cases(log_id, api_key, tfs=[]) -> int:
    """Returns the number of cases."""

    df = aggregate(api_key,
                   trace_filter_sequence=tfs,
                   log_id=log_id,
                   metric="frequency",
                   aggregation_function="sum"
                   )
    return int(df["frequency"].iloc[0])


def median_case_duration(log_id, api_key, tfs=[]) -> float:
    """Returns median case duration in seconds."""
    df = aggregate(api_key=api_key,
                   log_id=log_id,
                   trace_filter_sequence=tfs,
                   metric="duration",
                   aggregation_function="median"
                   )
    return float(df["duration"].values[0] / 1000)
