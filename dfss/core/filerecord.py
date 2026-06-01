from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict
import time
import uuid

from ..constants import DEFAULT_SCHEMA_VERSION
from .registry import SchemaRegistry


@dataclass
class FileRecord:
    """Stable core record object shared across all DFSS schemas."""

    id: str
    node_id: str
    global_id: str
    path: str
    type: str
    meta: Dict[str, Any] = field(default_factory=dict)
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)
    last_seen: float = field(default_factory=time.time)

    def __post_init__(self) -> None:
        if not isinstance(self.meta, dict):
            raise TypeError("meta must be a dictionary")
        self.meta = dict(self.meta)
        self._ensure_schema_meta()

    @classmethod
    def create(
        cls,
        *,
        path: str,
        type: str | None = None,
        record_type: str | None = None,
        meta: Dict[str, Any] | None = None,
        node_id: str = "local",
        global_id: str | None = None,
        schema_version: str | None = None,
        record_id: str | None = None,
    ) -> "FileRecord":
        resolved_type = type or record_type
        if not resolved_type:
            raise ValueError("type or record_type is required")

        now = time.time()
        record = cls(
            id=record_id or str(uuid.uuid4()),
            node_id=node_id,
            global_id=global_id or str(uuid.uuid4()),
            path=path,
            type=resolved_type,
            meta=meta or {},
            created_at=now,
            updated_at=now,
            last_seen=now,
        )
        record._ensure_schema_meta(schema_version=schema_version)
        return record

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FileRecord":
        required = {
            "id",
            "node_id",
            "global_id",
            "path",
            "type",
            "meta",
            "created_at",
            "updated_at",
            "last_seen",
        }
        missing = sorted(required - set(data.keys()))
        if missing:
            raise ValueError(f"Missing required field(s): {', '.join(missing)}")

        return cls(
            id=str(data["id"]),
            node_id=str(data["node_id"]),
            global_id=str(data["global_id"]),
            path=str(data["path"]),
            type=str(data["type"]),
            meta=dict(data["meta"]),
            created_at=float(data["created_at"]),
            updated_at=float(data["updated_at"]),
            last_seen=float(data["last_seen"]),
        )

    @property
    def schema_name(self) -> str:
        return self.meta.get("_schema", {}).get("name", self.type)

    @property
    def schema_version(self) -> str:
        return self.meta.get("_schema", {}).get("version", DEFAULT_SCHEMA_VERSION)

    def touch(self) -> None:
        now = time.time()
        self.last_seen = now
        self.updated_at = now

    def update(self, meta: Dict[str, Any] | None = None, *, merge: bool = True) -> None:
        if meta is not None:
            if merge:
                updated_meta = dict(self.meta)
                for key, value in meta.items():
                    if (
                        isinstance(updated_meta.get(key), dict)
                        and isinstance(value, dict)
                        and key != "_schema"
                    ):
                        updated_meta[key] = {**updated_meta[key], **value}
                    else:
                        updated_meta[key] = value
                self.meta = updated_meta
            else:
                self.meta = dict(meta)
        self._ensure_schema_meta()
        self.updated_at = time.time()
        self.last_seen = self.updated_at

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "node_id": self.node_id,
            "global_id": self.global_id,
            "path": self.path,
            "type": self.type,
            "meta": self.meta,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "last_seen": self.last_seen,
        }

    def validate(self) -> bool:
        from .validator import FileRecordValidator

        return FileRecordValidator.validate(self)

    def _ensure_schema_meta(self, schema_version: str | None = None) -> None:
        version = schema_version
        if version is None and SchemaRegistry.exists(self.type):
            version = SchemaRegistry.get_default_version(self.type)
        version = version or DEFAULT_SCHEMA_VERSION
        self.meta.setdefault("_schema", {})
        self.meta["_schema"]["name"] = self.type
        self.meta["_schema"]["version"] = version
