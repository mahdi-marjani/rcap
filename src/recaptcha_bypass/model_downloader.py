import requests
from tqdm import tqdm
from pathlib import Path

MODEL_URLS = {
    "crosswalk.pt": "https://github.com/mahdi-marjani/recaptcha-bypass/releases/download/v0.1.0/crosswalk.pt",
}


def download_model_if_missing(model_name: str, models_directory:Path):
    model_path = models_directory / model_name
    if model_path.exists():
        return

    url = MODEL_URLS.get(model_name)

    print(f"Downloading {model_name} ...")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024 * 1024  # 1MB

    with open(model_path, "wb") as f, tqdm(
        total=total_size, unit="iB", unit_scale=True, desc=model_name
    ) as pbar:
        for data in response.iter_content(block_size):
            f.write(data)
            pbar.update(len(data))

    print(f"{model_name} downloaded successfully!")
