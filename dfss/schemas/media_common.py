from __future__ import annotations

from typing import Any, Mapping

MEDIA_COMMON_FIELD_TYPES = {
    "file_name": object,
    "size": object,
    "mime_type": object,
}

MEDIA_COMMON_RELATION_TYPES = {
    "platform": object,
    "chat_id": object,
    "message_id": object,
}


def with_media_common_sections(
    schema: Mapping[str, Mapping[str, Any]],
    *,
    field_overrides: Mapping[str, Any] | None = None,
    relation_overrides: Mapping[str, Any] | None = None,
) -> dict[str, dict[str, Any]]:
    merged_schema: dict[str, dict[str, Any]] = {
        section_name: dict(section_fields)
        for section_name, section_fields in schema.items()
    }

    merged_fields = dict(MEDIA_COMMON_FIELD_TYPES)
    if field_overrides:
        merged_fields.update(field_overrides)
    merged_schema["fields"] = {
        **merged_fields,
        **merged_schema.get("fields", {}),
    }

    merged_relation = dict(MEDIA_COMMON_RELATION_TYPES)
    if relation_overrides:
        merged_relation.update(relation_overrides)
    merged_schema["relation"] = {
        **merged_relation,
        **merged_schema.get("relation", {}),
    }

    return merged_schema


__all__ = [
    "MEDIA_COMMON_FIELD_TYPES",
    "MEDIA_COMMON_RELATION_TYPES",
    "with_media_common_sections",
]
