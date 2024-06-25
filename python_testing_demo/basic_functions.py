def function_that_returns_text(text: str):
    if isinstance(text, str):
        return text
    else:
        raise ValueError(f"Input did not have a '{str}' type, but '{type(text)}'!")
