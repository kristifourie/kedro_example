# src/anomaly_example/pipelines/eda.py

from kedro.pipeline import Pipeline, node
from anomaly_example.nodes.raw import get_raw_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        #examples of nodes
        node(
            func=get_raw_data,
            inputs="gcp_pricing_data",
            outputs=None,
            name="raw_data"
        ),
        node(
            func=get_raw_data,
            inputs="gcp_pricing_data",
            outputs=None,
            name="processed_data"
        ),

    ])
