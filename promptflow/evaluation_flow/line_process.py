from promptflow.core import tool
import json

@tool
def line_process(groundtruth: float, prediction: str) -> bool:
    """
    This tool processes the prediction of a single line and returns the processed result.

    :param groundtruth: the groundtruth of a single line.
    :param prediction: the prediction of a single line.
    """

    return "Correct" if json.loads(prediction).get("score", 0.0) >= groundtruth else "Incorrect"
