from capx_client.solver import BaseRecaptchaSolver


class RecaptchaSolver(BaseRecaptchaSolver):
    def __init__(self, driver):
        super().__init__(driver)
        from .local_ai import is_model_available, detect
        self.is_model_available = is_model_available
        self.detect = detect