class AccountError(Exception):
    def __init__(self, message, required):
        super().__init__(message)
        self.required = required

class QuantityError(Exception):
    pass