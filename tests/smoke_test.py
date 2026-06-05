from dfss import FileRecord, SchemaRegistry
from dfss.schemas.article import build_article_record
from dfss.schemas.image import build_image_record
from dfss.schemas.music import build_music_record
from dfss.schemas.pdf import build_pdf_record
from dfss.schemas.site import build_site_record
from dfss.schemas.video import build_video_record


def main():
    supported = set(SchemaRegistry.types())
    assert {"article", "video", "pdf", "image", "audio", "music", "youtube_video", "url", "rss", "webpage", "site"}.issubset(supported)

    article = FileRecord.create(
        type="article",
        path="article.html",
        meta={
            "fields": {"title": "Hello", "author": "DFSS", "published_at": "2026-06-01", "summary": "test", "language": "ko", "source": "local"},
            "content": {"full_text": "본문", "excerpt": "요약"},
            "semantic": {"topics": ["dfss"], "keywords": ["schema"], "entities": ["FileRecord"]},
            "relation": {"source_url": "https://example.com", "parent_global_id": "root", "related_global_ids": []},
            "scoring": {"quality": 1.0, "relevance": 1.0, "confidence": 1.0},
        },
    )
    assert article.meta["_schema"]["name"] == "article"
    assert article.meta["_schema"]["version"] == "1.0"
    assert article.validate() is True

    built_article = build_article_record(path="post.html", meta={})
    assert built_article.type == "article"
    assert built_article.meta["_schema"]["version"] == "1.0"

    built_video = build_video_record(path="clip.mp4", meta={})
    assert built_video.type == "video"
    assert built_video.meta["_schema"]["name"] == "video"

    pdf = build_pdf_record(
        path="paper.pdf",
        meta={
            "fields": {
                "title": "Spec",
                "source_url": "https://example.com/spec.pdf",
                "snippet": "summary",
                "page_count": 12,
                "language": "ko",
            },
            "scoring": {"relevance": 0.9, "freshness": 0.8},
        },
    )
    assert pdf.validate() is True

    image = build_image_record(
        path="photo.jpg",
        meta={
            "fields": {
                "width": 1920,
                "height": 1080,
                "format": "jpg",
                "camera": "demo",
                "created_at": "2026-06-01T00:00:00Z",
            },
            "gps": {"lat": 37.5, "lon": 127.0, "alt": 10},
            "feature": {
                "scene": "street",
                "objects": ["car", "tree"],
                "dominant_color": "blue",
                "embedding": [0.1, 0.2],
            },
            "map": {"tile": "12/123/456", "geohash": "wydm6", "region": "seoul"},
        },
    )
    assert image.validate() is True

    site = build_site_record(
        path="https://example.com",
        meta={
            "fields": {
                "url": "https://example.com",
                "domain": "example.com",
                "title": "Example",
                "site_type": "docs",
                "language": "en",
                "framework": "static",
                "server": "nginx",
                "status_code": 200,
                "created_at": "2026-06-01T00:00:00Z",
                "crawled_at": "2026-06-01T00:05:00Z",
                "updated_at": "2026-06-01T00:10:00Z",
            },
            "structure": {
                "pages": ["/", "/docs"],
                "links": ["https://example.com/docs"],
                "resources": ["/app.js", "/app.css"],
                "api_endpoints": ["https://example.com/api/health"],
                "media_streams": [],
                "sitemaps": ["https://example.com/sitemap.xml"],
                "robots_txt": "User-agent: *",
            },
            "authentication": {
                "auth_required": False,
                "auth_type": "none",
                "login_endpoint": "",
                "session_type": "stateless",
            },
            "content": {
                "html": "<html></html>",
                "text": "Example site",
                "scripts": ["app.js"],
                "styles": ["app.css"],
            },
            "media": {
                "images": [],
                "videos": [],
                "audios": [],
                "documents": [],
            },
            "semantic": {
                "topics": ["docs"],
                "keywords": ["example"],
                "entities": ["Example"],
                "summary": "Example site",
                "embedding": [0.1, 0.2],
            },
            "relation": {
                "outbound_links": [],
                "inbound_links": [],
                "api_relations": [],
                "media_relations": [],
                "related_records": [],
            },
            "analysis": {
                "technology_stack": ["nginx", "static"],
                "content_category": "documentation",
                "crawl_depth": 2,
                "api_count": 1,
                "media_count": 0,
                "link_count": 1,
            },
            "scoring": {
                "importance_score": 0.8,
                "quality_score": 0.9,
                "freshness_score": 0.7,
                "authority_score": 0.6,
            },
        },
    )
    assert site.validate() is True

    music = build_music_record(
        path="song.mp3",
        meta={
            "fields": {
                "play_score": 100,
                "artist": "DFSS",
                "album": "Demo",
                "genre": "test",
                "duration": 180,
            }
        },
    )
    assert music.validate() is True

    print("smoke test passed")


if __name__ == "__main__":
    main()
