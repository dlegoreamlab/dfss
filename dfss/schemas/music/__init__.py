from .builder import build_music_record
from .schema import MUSIC_SCHEMA, SCHEMA_NAME, SCHEMA_VERSION, register_schema
from .validator import MusicRecordValidator

register_schema()

__all__ = [
    "MUSIC_SCHEMA",
    "SCHEMA_NAME",
    "SCHEMA_VERSION",
    "MusicRecordValidator",
    "build_music_record",
    "register_schema",
]
