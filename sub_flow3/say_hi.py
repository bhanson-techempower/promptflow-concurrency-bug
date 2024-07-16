from promptflow import tool


@tool
def say_hi(name: str) -> str:
    return f"Hi, {name}!"
