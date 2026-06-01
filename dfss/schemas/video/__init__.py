from .builder import build_video_record
from .schema import SCHEMA_NAME, SCHEMA_VERSION, VIDEO_SCHEMA, register_schema
from .validator import VideoRecordValidator

register_schema()

__all__ = [
    "VIDEO_SCHEMA",
    "SCHEMA_NAME",
    "SCHEMA_VERSION",
    "VideoRecordValidator",
    "build_video_record",
    "register_schema",
]
