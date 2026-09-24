from src.processing.normalizer import normalize_complaint


def test_normalize_complaint():

    complaint = {
        "odiNumber": "123456",
        "manufacturer": "Honda",
        "crash": "NO",
        "fire": "NO",
        "numberOfInjuries": 0,
        "numberOfDeaths": 0,
        "component": "BRAKES",
        "summary": "Vehicle shakes while braking.",
        "products": [
            {
                "productYear": "2021",
                "productMake": "HONDA",
                "productModel": "CIVIC",
                "manufacturer": "Honda",
            }
        ],
    }

    document = normalize_complaint(
        complaint
    )

    assert document.id == (
        "nhtsa_complaint_123456"
    )

    assert document.metadata.make == "HONDA"

    assert document.metadata.model == "CIVIC"

    assert document.metadata.model_year == 2021

    assert "Vehicle shakes while braking" in (
        document.text
    )