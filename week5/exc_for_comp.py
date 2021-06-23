class AddElemCompException(Exception):
    def __init__(self, text_exc: str):
        self.text_exc = text_exc


class CompTurnOnException(Exception):
    def __init__(self, text_exc: str):
        self.text_exc = text_exc


class DegreeDivisionError(Exception):
    def __init__(self, text_exc: str):
        self.text_exc = text_exc
