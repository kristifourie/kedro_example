"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline
from anomaly_example.pipelines.raw_data import create_pipeline as create_raw_pipeline

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    return {
        "__default__": create_raw_pipeline(),
        "raw": create_raw_pipeline(),
    }