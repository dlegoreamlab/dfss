from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry

SCHEMA_NAME = "image"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

IMAGE_SCHEMA = {
    "fields": {
        "width": object,
        "height": object,
        "format": object,
        "camera": object,
        "created_at": object,
    },
    "gps": {
        "lat": object,
        "lon": object,
        "alt": object,
    },
    "feature": {
        "scene": object,
        "objects": object,
        "dominant_color": object,
        "embedding": object,
    },
    "map": {
        "tile": object,
        "geohash": object,
        "region": object,
    },
}


def register_schema():
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=IMAGE_SCHEMA,
        )
