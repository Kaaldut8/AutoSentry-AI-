import requests

import json
from pathlib import Path



BASE_URL = "https://api.nhtsa.gov"


def get_complaints(make: str, model: str, model_year: int):
    url = f"{BASE_URL}/complaints/complaintsByVehicle"

    params = {
        "make": make,
        "model": model,
        "modelYear": model_year
    }

    response = requests.get(url, params, timeout=30)

    response.raise_for_status()

    return response.json()


def get_recalls(make: str, model: str, model_year: int):
    url = f"{BASE_URL}/recalls/recallsByVehicle"

    params = {
        "make": make,
        "model": model,
        "modelYear": model_year
    }

    response = requests.get(url, params, timeout=30)

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    data = get_complaints(
        make="Honda",
        model="Civic",
        model_year=2021
    )

    output_path = Path("data/raw/honda_civic_2021_complaints.json")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    data = get_recalls(
        make="Honda",
        model="Civic",
        model_year="2021"
    )

    output_path = Path("data/raw/honda_civic_2021_recalls.json")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)