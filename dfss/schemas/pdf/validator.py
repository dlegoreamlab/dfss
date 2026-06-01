from __future__ import annotations

from ...core.validator import FileRecordValidator


class PdfRecordValidator(FileRecordValidator):
    RECORD_TYPE = "pdf"
