from __future__ import annotations

from ...core.validator import FileRecordValidator


class ArticleRecordValidator(FileRecordValidator):
    RECORD_TYPE = "site"
