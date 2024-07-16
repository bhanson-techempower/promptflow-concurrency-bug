from promptflow.client import load_flow
from promptflow.core import tool


@tool
def run_sub_flow1(name: str) -> str:
    for _ in range(5):
        flow = load_flow("sub_flow1")
    outputs = flow(name=name)
    return outputs
