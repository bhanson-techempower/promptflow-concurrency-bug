from promptflow import tool


@tool
def say_howdi(name: str) -> str:
    return f"Howdi, {name}!"
