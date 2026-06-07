from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry
from ..media_common import with_media_common_sections

SCHEMA_NAME = "music"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

MUSIC_SCHEMA = with_media_common_sections(
    {
        "fields": {
            "play_score": object,
            "artist": object,
            "album": object,
            "genre": object,
            "duration": object,
        },
        "relation": {},
    }
)


def register_schema():
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=MUSIC_SCHEMA,
        )
