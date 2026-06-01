from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry

SCHEMA_NAME = "pdf"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

PDF_SCHEMA = {
    "fields": {
        "title": object,
        "source_url": object,
        "snippet": object,
        "page_count": object,
        "language": object,
    },
    "scoring": {
        "relevance": object,
        "freshness": object,
    },
}


def register_schema():
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=PDF_SCHEMA,
        )
