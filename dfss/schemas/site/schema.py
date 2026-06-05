from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry

SCHEMA_NAME = "site"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

SITE_SCHEMA = {
    "fields": {
        "url": str,
        "domain": str,
        "title": str,
        "site_type": str,
        "language": str,
        "framework": str,
        "server": str,
        "status_code": int,
        "created_at": str,
        "crawled_at": str,
        "updated_at": str,
    },
    "structure": {
        "pages": list,
        "links": list,
        "resources": list,
        "api_endpoints": list,
        "media_streams": list,
        "sitemaps": list,
        "robots_txt": str,
    },
    "authentication": {
        "auth_required": bool,
        "auth_type": str,
        "login_endpoint": str,
        "session_type": str,
    },
    "content": {
        "html": str,
        "text": str,
        "scripts": list,
        "styles": list,
    },
    "media": {
        "images": list,
        "videos": list,
        "audios": list,
        "documents": list,
    },
    "semantic": {
        "topics": list,
        "keywords": list,
        "entities": list,
        "summary": str,
        "embedding": list,
    },
    "relation": {
        "outbound_links": list,
        "inbound_links": list,
        "api_relations": list,
        "media_relations": list,
        "related_records": list,
    },
    "analysis": {
        "technology_stack": list,
        "content_category": str,
        "crawl_depth": int,
        "api_count": int,
        "media_count": int,
        "link_count": int,
    },
    "scoring": {
        "importance_score": (int, float),
        "quality_score": (int, float),
        "freshness_score": (int, float),
        "authority_score": (int, float),
    },
}


def register_schema() -> None:
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=SITE_SCHEMA,
        )
