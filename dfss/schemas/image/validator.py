from __future__ import annotations

from ...core.validator import FileRecordValidator


class ImageRecordValidator(FileRecordValidator):
    RECORD_TYPE = "image"
