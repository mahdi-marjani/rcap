from capx_client.solver import BaseRecaptchaSolver
from capx_core.detector import detect_cells
from capx_core.models import AVAILABLE_MODELS


class RecaptchaSolver(BaseRecaptchaSolver):
    def __init__(self, driver):
        super().__init__(driver)
        self.available_models = AVAILABLE_MODELS

    def is_model_available(self, target_text):
        target_text = target_text.lower()
        return any(model in target_text for model in self.available_models)

    def detect(self, image_array, grid, target_text):
        return detect_cells(image_array, grid, target_text)