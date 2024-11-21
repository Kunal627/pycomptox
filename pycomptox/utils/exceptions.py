class APIRequestError(Exception):
    """
    Raised when an API request fails.
    """
    def __init__(self, message: str):
        super().__init__(message)
