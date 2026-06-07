from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry
from ..media_common import with_media_common_sections

SCHEMA_NAME = "video"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

VIDEO_SCHEMA = with_media_common_sections(
    {
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
    },
    field_overrides={
        "file_name": str,
        "size": int,
        "mime_type": str,
    },
    relation_overrides={
        "platform": str,
        "chat_id": int,
        "message_id": int,
    },
)


def register_schema():
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=VIDEO_SCHEMA,
        )
