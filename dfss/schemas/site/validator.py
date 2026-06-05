from __future__ import annotations

from ...core.validator import FileRecordValidator


class SiteRecordValidator(FileRecordValidator):
    RECORD_TYPE = "site"
