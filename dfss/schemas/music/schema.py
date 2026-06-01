from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry

SCHEMA_NAME = "music"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

MUSIC_SCHEMA = {
    "fields": {
        "play_score": object,
        "artist": object,
        "album": object,
        "genre": object,
        "duration": object,
    },
}


def register_schema():
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=MUSIC_SCHEMA,
        )
