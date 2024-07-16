from promptflow import tool


@tool
def say_hello(name: str) -> str:
    return f"Hello, {name}!"
