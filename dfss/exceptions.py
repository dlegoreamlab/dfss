class DFSSException(Exception):
    """Base exception for the DFSS package."""


class ValidationError(DFSSException):
    """Raised when a FileRecord does not match its schema."""


class SchemaRegistrationError(DFSSException):
    """Raised when a schema cannot be registered."""


class UnknownSchemaError(DFSSException, KeyError):
    """Raised when a schema is not registered."""
