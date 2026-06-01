from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Mapping

from ..constants import DEFAULT_SCHEMA_VERSION
from ..exceptions import SchemaRegistrationError, UnknownSchemaError


@dataclass(frozen=True)
class SchemaDefinition:
    name: str
    version: str
    sections: Mapping[str, Mapping[str, Any]]


class SchemaRegistry:
    """Registry for DFSS schema plugins."""

    _schemas: Dict[str, Dict[str, SchemaDefinition]] = {}
    _builtins_loaded: bool = False

    @classmethod
    def register(
        cls,
        name: str,
        sections: Mapping[str, Mapping[str, Any]],
        version: str = DEFAULT_SCHEMA_VERSION,
        *,
        overwrite: bool = False,
    ) -> SchemaDefinition:
        if not name:
            raise SchemaRegistrationError("schema name is required")
        if not isinstance(sections, Mapping):
            raise SchemaRegistrationError("schema sections must be a mapping")

        version_map = cls._schemas.setdefault(name, {})
        if version in version_map and not overwrite:
            raise SchemaRegistrationError(
                f"Schema already registered: {name}@{version}"
            )

        definition = SchemaDefinition(name=name, version=version, sections=dict(sections))
        version_map[version] = definition
        return definition

    @classmethod
    def get(cls, name: str, version: str | None = None) -> SchemaDefinition:
        cls._ensure_builtins_loaded()
        if name not in cls._schemas:
            raise UnknownSchemaError(f"Unknown schema: {name}")

        version_map = cls._schemas[name]
        target_version = version or cls.get_default_version(name)
        if target_version not in version_map:
            raise UnknownSchemaError(f"Unknown schema version: {name}@{target_version}")
        return version_map[target_version]

    @classmethod
    def exists(cls, name: str, version: str | None = None) -> bool:
        cls._ensure_builtins_loaded()
        if name not in cls._schemas:
            return False
        if version is None:
            return True
        return version in cls._schemas[name]

    @classmethod
    def types(cls) -> list[str]:
        cls._ensure_builtins_loaded()
        return sorted(cls._schemas.keys())

    @classmethod
    def versions(cls, name: str) -> list[str]:
        cls._ensure_builtins_loaded()
        if name not in cls._schemas:
            raise UnknownSchemaError(f"Unknown schema: {name}")
        return sorted(cls._schemas[name].keys())

    @classmethod
    def get_default_version(cls, name: str) -> str:
        if name not in cls._schemas:
            raise UnknownSchemaError(f"Unknown schema: {name}")
        versions = sorted(cls._schemas[name].keys())
        return versions[-1]

    @classmethod
    def clear(cls) -> None:
        cls._schemas.clear()
        cls._builtins_loaded = False

    @classmethod
    def _ensure_builtins_loaded(cls) -> None:
        if cls._builtins_loaded:
            return
        from .. import schemas  # noqa: F401

        cls._builtins_loaded = True
