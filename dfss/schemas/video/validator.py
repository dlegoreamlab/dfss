from __future__ import annotations

from ...core.validator import FileRecordValidator


class VideoRecordValidator(FileRecordValidator):
    RECORD_TYPE = "video"
