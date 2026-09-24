from pydantic import BaseModel, Field



class ComplaintMetadata(BaseModel):
    source: str = "nhtsa"
    document_type: str = "complaint"

    odi_number: str | None = None

    make: str | None = None
    model: str | None = None
    model_year: int | None = None

    manufacturer: str | None = None
    component: str | None = None

    crash: bool | None = None
    fire: bool | None = None

    injuries: int = 0
    deaths: int = 0


class AutoSentryDocument(BaseModel):
    id: str
    text: str
    metadata: ComplaintMetadata