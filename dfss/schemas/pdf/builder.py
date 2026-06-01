from __future__ import annotations

from typing import Any, Dict

from ...core.builder import FileRecordBuilder


def build_pdf_record(
    path: str,
    meta: Dict[str, Any] | None = None,
    *,
    node_id: str = "local",
    schema_version: str | None = None,
    validate: bool = True,
):
    return FileRecordBuilder.build(
        record_type="pdf",
        path=path,
        meta=meta or {},
        node_id=node_id,
        schema_version=schema_version,
        validate=validate,
    )
