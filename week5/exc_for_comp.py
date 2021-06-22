class AddElemCompException(Exception):
    def __init__(self, text_exc: str):
        self.text_exc = text_exc


class CompTurnOnException(Exception):
    def __init__(self, text_exc: str):
        self.text_exc = text_exc


class DegreeTwoDivisionError(Exception):
    def __init__(self, text_exc: str):
        self.text_exc = text_exc
