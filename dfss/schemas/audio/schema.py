from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry

SCHEMA_NAME = "audio"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

# Field types use `object` (matching IMAGE_SCHEMA / PDF_SCHEMA conventions) so that
# nullable / optional values are accepted while still enforcing the allowed field
# key set. This keeps audio records compatible with upstream producers such as DICL,
# which may legitimately leave some metadata as None until later enrichment stages.
AUDIO_SCHEMA = {
    "fields": {
        "title": object,
        "codec": object,
        "duration_sec": object,
        "sample_rate": object,
        "channels": object,
        "language": object,
    },
    "content": {
        "transcript": object,
        "summary": object,
    },
    "semantic": {
        "topics": object,
        "keywords": object,
        "speakers": object,
    },
    "relation": {
        "source_url": object,
        "derived_from": object,
        "segments": object,
    },
    "scoring": {
        "quality": object,
        "transcription_confidence": object,
    },
}


def register_schema():
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=AUDIO_SCHEMA,
        )
