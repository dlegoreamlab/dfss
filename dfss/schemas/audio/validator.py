from __future__ import annotations

from ...core.validator import FileRecordValidator


class AudioRecordValidator(FileRecordValidator):
    RECORD_TYPE = "audio"
