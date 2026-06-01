from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry

SCHEMA_NAME = "article"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

ARTICLE_SCHEMA = {
    "fields": {
        "title": str,
        "author": str,
        "published_at": str,
        "summary": str,
        "language": str,
        "source": str,
    },
    "content": {
        "full_text": str,
        "excerpt": str,
    },
    "semantic": {
        "topics": list,
        "keywords": list,
        "entities": list,
    },
    "relation": {
        "source_url": str,
        "parent_global_id": str,
        "related_global_ids": list,
    },
    "scoring": {
        "quality": (int, float),
        "relevance": (int, float),
        "confidence": (int, float),
    },
}


def register_schema():
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=ARTICLE_SCHEMA,
        )
