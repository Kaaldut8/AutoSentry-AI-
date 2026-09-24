from src.processing.models import (
    AutoSentryDocument,
    ComplaintMetadata,
)


def normalize_complaint(
    complaint: dict,
) -> AutoSentryDocument:

    product = {}

    products = complaint.get("products") or []

    if products:
        product = products[0]

    make = product.get("productMake")
    model = product.get("productModel")
    year = product.get("productYear")

    model_year = None

    if year:
        try:
            model_year = int(year)
        except (TypeError, ValueError):
            model_year = None

        metadata = ComplaintMetadata(
        odi_number=str(
            complaint.get("odiNumber")
        ) if complaint.get("odiNumber") else None,

        make=make,
        model=model,
        model_year=model_year,

        manufacturer=complaint.get(
            "manufacturer"
        ),

        component=complaint.get(
            "component"
        ),

        crash=complaint.get("crash"),
        fire=complaint.get("fire"),

        injuries=int(
            complaint.get(
                "numberOfInjuries"
            ) or 0
        ),

        deaths=int(
            complaint.get(
                "numberOfDeaths"
            ) or 0
        ),
    )

    summary = complaint.get(
        "summary",
        ""
    )

    text = f"""
Vehicle:
{model_year} {make} {model}

Manufacturer:
{metadata.manufacturer}

Component:
{metadata.component}

Consumer Complaint:
{summary}
""".strip()

    document_id = (
        f"nhtsa_complaint_"
        f"{metadata.odi_number}"
    )

    return AutoSentryDocument(
        id=document_id,
        text=text,
        metadata=metadata,
    )