from .article import ARTICLE_SCHEMA
from .builtin import (
    AUDIO_SCHEMA,
    BUILTIN_SCHEMAS,
    RSS_SCHEMA,
    URL_SCHEMA,
    WEBPAGE_SCHEMA,
    YOUTUBE_VIDEO_SCHEMA,
    register_builtin_schemas,
)
from .image import IMAGE_SCHEMA
from .music import MUSIC_SCHEMA
from .pdf import PDF_SCHEMA
from .video import VIDEO_SCHEMA

register_builtin_schemas()

__all__ = [
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
    "BUILTIN_SCHEMAS",
    "register_builtin_schemas",
]
