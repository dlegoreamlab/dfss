from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry

SCHEMA_NAME = "video"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

VIDEO_SCHEMA = {
    "fields": {
        "title": str,
        "codec": str,
        "duration_sec": (int, float),
        "width": int,
        "height": int,
        "fps": (int, float),
        "language": str,
    },
    "content": {
        "transcript": str,
        "summary": str,
        "captions": list,
    },
    "semantic": {
        "topics": list,
        "keywords": list,
        "scenes": list,
    },
    "relation": {
        "source_url": str,
        "thumbnail_path": str,
        "chapters": list,
    },
    "scoring": {
        "quality": (int, float),
        "classification_confidence": (int, float),
    },
}


def register_schema():
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=VIDEO_SCHEMA,
        )
