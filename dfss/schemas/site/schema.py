from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry

SCHEMA_NAME = "site"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

# Field types use `object` (matching IMAGE_SCHEMA / PDF_SCHEMA conventions) so that
# nullable / partially-populated metadata is accepted while still enforcing the allowed
# field key set. Site records are typically produced by crawlers (e.g. DICL) at varying
# enrichment stages, so strict type enforcement on every field would reject otherwise
# valid records that have not yet completed their analysis pipeline.
SITE_SCHEMA = {
    "fields": {
        "url": object,
        "domain": object,
        "title": object,
        "site_type": object,
        "language": object,
        "framework": object,
        "server": object,
        "status_code": object,
        "created_at": object,
        "crawled_at": object,
        "updated_at": object,
    },
    "structure": {
        "pages": object,
        "links": object,
        "resources": object,
        "api_endpoints": object,
        "media_streams": object,
        "sitemaps": object,
        "robots_txt": object,
    },
    "authentication": {
        "auth_required": object,
        "auth_type": object,
        "login_endpoint": object,
        "session_type": object,
    },
    "content": {
        "html": object,
        "text": object,
        "scripts": object,
        "styles": object,
    },
    "media": {
        "images": object,
        "videos": object,
        "audios": object,
        "documents": object,
    },
    "semantic": {
        "topics": object,
        "keywords": object,
        "entities": object,
        "summary": object,
        "embedding": object,
    },
    "relation": {
        "outbound_links": object,
        "inbound_links": object,
        "api_relations": object,
        "media_relations": object,
        "related_records": object,
    },
    "analysis": {
        "technology_stack": object,
        "content_category": object,
        "crawl_depth": object,
        "api_count": object,
        "media_count": object,
        "document_count": object,
        "link_count": object,
    },
    "scoring": {
        "importance_score": object,
        "quality_score": object,
        "freshness_score": object,
        "authority_score": object,
    },
}


def register_schema() -> None:
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=SITE_SCHEMA,
        )
