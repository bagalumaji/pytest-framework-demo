class BrowserNotSupportedError(RuntimeError):
    def __init__(self, browser_name):
        super().__init__(f"'{browser_name}' is not a supported browser.")
