import json
from pathlib import Path

from src.processing.normalizer import normalize_complaint


def build_complaint_dataset(
    input_path: str,
    output_path: str,
):

    with open(
        input_path,
        encoding="utf-8",
    ) as f:
        data = json.load(f)

    documents = []

    for complaint in data["results"]:

        try:
            document = normalize_complaint(
                complaint
            )

            documents.append(document)

        except Exception as exc:
            print(
                f"Failed to process complaint: {exc}"
            )

    output = Path(output_path)

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output.open(
        "w",
        encoding="utf-8",
    ) as f:

        for document in documents:

            f.write(
                document.model_dump_json()
                + "\n"
            )

    print(
        f"Processed {len(documents)} documents."
    )



if __name__ == "__main__":
    build_complaint_dataset(
        input_path=(
            "data/raw/"
            "honda_civic_2021_complaints.json"
        ),
        output_path=(
            "data/processed/"
            "nhtsa_complaints.jsonl"
        ),
    )