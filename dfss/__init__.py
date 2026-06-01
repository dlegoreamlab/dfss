from .constants import PACKAGE_VERSION
from .core import FileRecord, FileRecordBuilder, FileRecordValidator, SchemaDefinition, SchemaRegistry
from .exceptions import DFSSException, SchemaRegistrationError, UnknownSchemaError, ValidationError
from .schemas import (
    ARTICLE_SCHEMA,
    AUDIO_SCHEMA,
    IMAGE_SCHEMA,
    MUSIC_SCHEMA,
    PDF_SCHEMA,
    RSS_SCHEMA,
    URL_SCHEMA,
    VIDEO_SCHEMA,
    WEBPAGE_SCHEMA,
    YOUTUBE_VIDEO_SCHEMA,
)

__version__ = PACKAGE_VERSION

__all__ = [
    "FileRecord",
    "FileRecordBuilder",
    "FileRecordValidator",
    "SchemaDefinition",
    "SchemaRegistry",
    "DFSSException",
    "ValidationError",
    "SchemaRegistrationError",
    "UnknownSchemaError",
    "ARTICLE_SCHEMA",
    "VIDEO_SCHEMA",
    "PDF_SCHEMA",
    "IMAGE_SCHEMA",
    "AUDIO_SCHEMA",
    "MUSIC_SCHEMA",
    "YOUTUBE_VIDEO_SCHEMA",
    "URL_SCHEMA",
    "RSS_SCHEMA",
    "WEBPAGE_SCHEMA",
]
