from __future__ import annotations

from ...core.validator import FileRecordValidator


class MusicRecordValidator(FileRecordValidator):
    RECORD_TYPE = "music"
