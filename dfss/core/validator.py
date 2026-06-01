from __future__ import annotations

from typing import Any

from ..constants import ALLOWED_META_SECTIONS
from ..exceptions import ValidationError
from .registry import SchemaRegistry


class FileRecordValidator:
    """Validate FileRecord instances against registered schema plugins."""

    @classmethod
    def validate(cls, record) -> bool:
        if not isinstance(record.path, str) or not record.path:
            raise ValidationError("path must be a non-empty string")
        if not isinstance(record.type, str) or not record.type:
            raise ValidationError("type must be a non-empty string")
        if not isinstance(record.meta, dict):
            raise ValidationError("meta must be a dictionary")

        schema_meta = record.meta.get("_schema")
        if not isinstance(schema_meta, dict):
            raise ValidationError("meta['_schema'] must be a dictionary")

        schema_name = schema_meta.get("name")
        schema_version = schema_meta.get("version")
        if schema_name != record.type:
            raise ValidationError("meta['_schema'].name must match record.type")
        if not isinstance(schema_version, str) or not schema_version:
            raise ValidationError("meta['_schema'].version must be a non-empty string")

        definition = SchemaRegistry.get(schema_name, schema_version)

        unknown_sections = set(record.meta.keys()) - ALLOWED_META_SECTIONS
        if unknown_sections:
            raise ValidationError(
                f"Unknown meta section(s): {', '.join(sorted(unknown_sections))}"
            )

        for section, expected_fields in definition.sections.items():
            if section not in record.meta:
                continue
            section_data = record.meta[section]
            if not isinstance(section_data, dict):
                raise ValidationError(f"{section} must be a dictionary")
            for field_name, field_value in section_data.items():
                if field_name not in expected_fields:
                    raise ValidationError(
                        f"{record.type}.{section}.{field_name} is not allowed"
                    )
                expected_type = expected_fields[field_name]
                if not cls._is_instance(field_value, expected_type):
                    expected_repr = cls._type_name(expected_type)
                    actual_repr = type(field_value).__name__
                    raise ValidationError(
                        f"{record.type}.{section}.{field_name} expected {expected_repr}, got {actual_repr}"
                    )
        return True

    @staticmethod
    def _is_instance(value: Any, expected_type: Any) -> bool:
        if isinstance(expected_type, tuple):
            return isinstance(value, expected_type)
        return isinstance(value, expected_type)

    @staticmethod
    def _type_name(expected_type: Any) -> str:
        if isinstance(expected_type, tuple):
            return " | ".join(t.__name__ for t in expected_type)
        return expected_type.__name__
