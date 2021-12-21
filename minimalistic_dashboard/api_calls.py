import requests
import argparse
import ast

from dashboard_components.api_abstraction import aggregate

def number_of_cases(log_id, auth_token, tfs=[]) -> int:
    """Returns the number of cases."""

    df = aggregate(auth_token,
                   trace_filter_sequence=tfs,
                   log_id=log_id,
                   metric="frequency",
                   aggregation_function="sum"
                   )
    return int(df["frequency"].iloc[0])


