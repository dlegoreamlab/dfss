from __future__ import annotations

from ..constants import DEFAULT_SCHEMA_VERSION
from ..core.registry import SchemaRegistry
# Backward-compat: AUDIO_SCHEMA was previously defined here.
# It now lives in `dfss.schemas.audio` (the audio sub-package), and is re-exported here
# so that `from dfss.schemas.builtin import AUDIO_SCHEMA` keeps working.
from .audio import AUDIO_SCHEMA  # noqa: F401

YOUTUBE_VIDEO_SCHEMA = {
    "fields": {
        "title": str,
        "channel": str,
        "published_at": str,
        "duration_sec": (int, float),
        "view_count": int,
        "language": str,
    },
    "content": {
        "description": str,
        "transcript": str,
    },
    "semantic": {
        "topics": list,
        "keywords": list,
        "entities": list,
    },
    "relation": {
        "video_url": str,
        "channel_url": str,
        "related_global_ids": list,
    },
    "scoring": {
        "engagement": (int, float),
        "quality": (int, float),
    },
}

URL_SCHEMA = {
    "fields": {
        "title": str,
        "domain": str,
        "published_at": str,
        "language": str,
    },
    "content": {
        "full_text": str,
        "html": str,
    },
    "semantic": {
        "topics": list,
        "keywords": list,
    },
    "relation": {
        "canonical_url": str,
        "redirect_chain": list,
        "parent_global_id": str,
    },
    "scoring": {
        "quality": (int, float),
        "crawl_confidence": (int, float),
    },
}

RSS_SCHEMA = {
    "fields": {
        "title": str,
        "site_name": str,
        "language": str,
        "updated_at_iso": str,
    },
    "content": {
        "entries": list,
        "description": str,
    },
    "semantic": {
        "topics": list,
        "keywords": list,
    },
    "relation": {
        "feed_url": str,
        "site_url": str,
    },
    "scoring": {
        "freshness": (int, float),
        "quality": (int, float),
    },
}

WEBPAGE_SCHEMA = {
    "fields": {
        "title": str,
        "domain": str,
        "status_code": int,
        "language": str,
        "fetched_at_iso": str,
    },
    "content": {
        "html": str,
        "markdown": str,
        "text": str,
    },
    "semantic": {
        "topics": list,
        "keywords": list,
        "entities": list,
    },
    "relation": {
        "canonical_url": str,
        "out_links": list,
        "in_links": list,
    },
    "scoring": {
        "quality": (int, float),
        "crawl_confidence": (int, float),
    },
}

BUILTIN_SCHEMAS = {
    "youtube_video": YOUTUBE_VIDEO_SCHEMA,
    "url": URL_SCHEMA,
    "rss": RSS_SCHEMA,
    "webpage": WEBPAGE_SCHEMA,
}


def register_builtin_schemas() -> None:
    for name, schema in BUILTIN_SCHEMAS.items():
        if not SchemaRegistry.exists(name, DEFAULT_SCHEMA_VERSION):
            SchemaRegistry.register(name=name, version=DEFAULT_SCHEMA_VERSION, sections=schema)
