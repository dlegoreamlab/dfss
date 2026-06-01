from __future__ import annotations

from typing import Any, Dict

from .filerecord import FileRecord
from .validator import FileRecordValidator


class FileRecordBuilder:
    """Factory for creating validated FileRecord objects."""

    @staticmethod
    def build(
        *,
        record_type: str,
        path: str,
        meta: Dict[str, Any] | None = None,
        node_id: str = "local",
        schema_version: str | None = None,
        validate: bool = True,
    ) -> FileRecord:
        record = FileRecord.create(
            type=record_type,
            path=path,
            meta=meta or {},
            node_id=node_id,
            schema_version=schema_version,
        )
        if validate:
            FileRecordValidator.validate(record)
        return record
