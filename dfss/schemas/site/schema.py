from __future__ import annotations

from ...constants import DEFAULT_SCHEMA_VERSION
from ...core.registry import SchemaRegistry

SCHEMA_NAME = "article"
SCHEMA_VERSION = DEFAULT_SCHEMA_VERSION

SITE_SCHEMA = {

    "site": {

        # ==========================================
        # 기본 정보
        # ==========================================

        "fields": [

            "url",
            "domain",
            "title",

            "site_type",      # blog, news, video, forum...
            "language",

            "framework",      # react, vue, django...
            "server",

            "status_code",

            "created_at",
            "crawled_at",
            "updated_at"
        ],

        # ==========================================
        # 구조 정보
        # ==========================================

        "structure": [

            "pages",
            "links",
            "resources",

            "api_endpoints",

            "media_streams",

            "sitemaps",

            "robots_txt"
        ],

        # ==========================================
        # 인증 정보
        # ==========================================

        "authentication": [

            "auth_required",

            "auth_type",      # none, cookie, jwt, oauth

            "login_endpoint",

            "session_type"
        ],

        # ==========================================
        # 콘텐츠
        # ==========================================

        "content": [

            "html",

            "text",

            "scripts",

            "styles"
        ],

        # ==========================================
        # 미디어
        # ==========================================

        "media": [

            "images",

            "videos",

            "audios",

            "documents"
        ],

        # ==========================================
        # 의미 정보
        # ==========================================

        "semantic": [

            "topics",

            "keywords",

            "entities",

            "summary",

            "embedding"
        ],

        # ==========================================
        # 관계 그래프
        # ==========================================

        "relations": [

            "outbound_links",

            "inbound_links",

            "api_relations",

            "media_relations",

            "related_records"
        ],

        # ==========================================
        # 분석 결과
        # ==========================================

        "analysis": [

            "technology_stack",

            "content_category",

            "crawl_depth",

            "api_count",

            "media_count",

            "link_count"
        ],

        # ==========================================
        # 점수
        # ==========================================

        "scoring": [

            "importance_score",

            "quality_score",

            "freshness_score",

            "authority_score"
        ]
    }
}

def register_schema():
    if not SchemaRegistry.exists(SCHEMA_NAME, SCHEMA_VERSION):
        SchemaRegistry.register(
            name=SCHEMA_NAME,
            version=SCHEMA_VERSION,
            sections=ARTICLE_SCHEMA,
        )
