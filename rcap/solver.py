from rcap_client.solver import RecaptchaSolver
from rcap_client.selenium import SeleniumBrowser
from rcap_client.playwright import PlaywrightBrowser
from rcap_core.detector import detect_cells
from rcap_core.models import AVAILABLE_MODELS


class Detector:
    """Detector that uses rcap-core models."""

    def is_model_available(self, target_text):
        target_text = target_text.lower()
        return any(model in target_text for model in AVAILABLE_MODELS)

    def detect(self, image_array, grid, target_text):
        return detect_cells(image_array, grid, target_text)


class SeleniumRecaptchaSolver(RecaptchaSolver):

    def __init__(self, driver):
        super().__init__(
            browser=SeleniumBrowser(driver),
            detector=Detector(),
        )


class PlaywrightRecaptchaSolver(RecaptchaSolver):

    def __init__(self, page):
        super().__init__(
            browser=PlaywrightBrowser(page),
            detector=Detector(),
        )
