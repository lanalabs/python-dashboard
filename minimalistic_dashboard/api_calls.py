import json
import pylana

from app import config
from dashboard_components.api_abstraction import aggregate

def number_of_cases(log_id, api_key, tfs=[]) -> int:
    """Returns the number of cases."""

    df = aggregate(api_key,
                   trace_filter_sequence=tfs,
                   log_id=log_id,
                   metric="frequency",
                   aggregation_function="sum"
                   )
    return int(df["frequency"].iloc[0])
