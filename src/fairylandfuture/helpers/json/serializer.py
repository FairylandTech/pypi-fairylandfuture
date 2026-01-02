# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-14 10:48:20 UTC+08:00
"""

import json
import typing as t
from decimal import Decimal

import orjson

from fairylandfuture import logger
from fairylandfuture.helpers.json.encoder import JsonEncoder

T = t.TypeVar("T")
ClazzType = t.TypeVar("ClazzType")
StrAny = t.TypeVar("StrAny", str, bytes, bytearray)


class JsonSerializerHelper:
    """
    Helper class for JSON serialization and deserialization.

    This class provides utility methods for serializing objects to JSON strings and
    deserializing JSON strings or dictionaries into Python objects. It leverages the
    `json` module for processing JSON data and supports custom class deserialization.
    """

    @classmethod
    def serialize(cls, value):
        """
        Serializes a given Python object into a JSON-formatted string. The method ensures that
        the serialization process adheres to specific formatting rules, including sorting keys,
        disabling ASCII-only encoding, and using a custom JSON encoder. This is particularly useful
        for maintaining consistent JSON output across various operations.

        :param value: The Python object to serialize. Can include data types such as dictionaries,
            lists, strings, integers, and custom objects supported by the specified JSON encoder.
        :type value: Any
        :return: A JSON-formatted string representation of the input value.
        :rtype: str
        """
        logger.debug(f"Serializing value of type {type(value)}")
        return json.dumps(value, cls=JsonEncoder, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

    @classmethod
    def deserialize(cls, value: StrAny | dict[str, t.Any], clazz: t.Callable[..., ClazzType] | None = None) -> ClazzType:
        """
        Deserialize a value into a Python object, optionally using a provided class type.

        This method allows for the deserialization of either JSON strings or dictionaries
        into Python objects. If a specific class is provided, the data will be used to create
        an instance of that class. If no class is provided, the method defaults to returning
        a dictionary when deserializing JSON strings.

        :param value: The input data to deserialize. Can be either a dictionary or a JSON string.
        :type value: Union[Dict[str, Any], str]
        :param clazz: An optional callable that specifies the class to which the value should
            be deserialized. If provided, value will be converted to an instance of this class.
        :type clazz: Optional[Callable[..., ClazzType]]
        :return: The deserialized object, which may be either a dictionary or an instance of the specified class.
        :rtype: ClazzType
        """
        logger.debug(f"Deserializing value of type {type(value)} to class {clazz}")
        if isinstance(value, dict):
            if not clazz:
                return value
            logger.debug(f"Deserializing dict to class {clazz}")
            return clazz(**value)

        if not clazz:
            logger.debug("No class provided, deserializing to dict")
            return json.loads(value)

        logger.debug(f"Deserializing to class {clazz} using object_hook")
        return json.loads(value, object_hook=lambda x: clazz(**x))


class OrjsonSerializerHelper:
    """
    Helper class for JSON serialization and deserialization using orjson.

    High-performance replacement for standard json library.
    """

    @classmethod
    def _default_encoder(cls, obj: t.Any) -> t.Any:
        """
        Custom default encoder for types not natively supported by orjson.
        Example: Decimals or custom classes with a to_dict method.
        """
        if isinstance(obj, Decimal):
            return float(obj)  # or str(obj) depending on precision needs
        if hasattr(obj, "to_dict"):
            return obj.to_dict()
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

    @classmethod
    def serialize(cls, value: t.Any, ensure_ascii: bool = False) -> str:
        """
        Serializes a Python object into a JSON-formatted STRING.

        Note: orjson natively returns bytes. This method decodes it to str to maintain
        compatibility with standard json behavior. For better performance, use serialize_bytes.
        """
        # OPT_SORT_KEYS: Sort keys (matches your original sort_keys=True)
        # OPT_NAIVE_UTC: Interpret naive datetime as UTC
        # OPT_UTC_Z: Append 'Z' to UTC datetime
        option = orjson.OPT_SORT_KEYS | orjson.OPT_NAIVE_UTC | orjson.OPT_UTC_Z

        # orjson handles datetime, uuid, dataclasses natively.
        # For others, we pass the fallback encoder.
        try:
            json_bytes = orjson.dumps(value, default=cls._default_encoder, option=option)
            return json_bytes.decode("utf-8")
        except Exception as error:
            logger.error(f"Serialization failed: {error}")
            raise

    @classmethod
    def serialize_bytes(cls, value: t.Any) -> bytes:
        """
        Serializes a Python object directly to JSON BYTES.
        This is faster than serialize() as it avoids the string decoding overhead.
        Recommended for network transmission (e.g., HTTP responses).
        """
        option = orjson.OPT_SORT_KEYS | orjson.OPT_NAIVE_UTC | orjson.OPT_UTC_Z
        return orjson.dumps(value, default=cls._default_encoder, option=option)

    @classmethod
    def deserialize(cls, value: str | bytes | dict[str, t.Any], clazz: type[T] | None = None) -> T | dict | list:
        """
        Deserialize a value into a Python object, optionally converting to a specific class.

        :param value: JSON string, bytes, or dictionary.
        :param clazz: Optional class type. If provided, the dict will be unpacked into this class.
        """
        if value is None:
            return None

        data = value

        # 1. Parse JSON if input is str or bytes
        if isinstance(value, (str, bytes)):
            try:
                data = orjson.loads(value)
            except orjson.JSONDecodeError as error:
                logger.error(f"Deserialization failed: {error}")
                raise ValueError("Invalid JSON format") from error

        # 2. Convert to class instance if clazz is provided
        if clazz:
            if isinstance(data, dict):
                # logger.debug(f"Converting dict to class {clazz.__name__}")
                try:
                    # Support Pydantic models (recommended) or standard classes
                    if hasattr(clazz, "model_validate"):  # Pydantic v2
                        return clazz.model_validate(data)
                    elif hasattr(clazz, "parse_obj"):  # Pydantic v1
                        return clazz.parse_obj(data)
                    else:
                        # Standard class via __init__(**kwargs)
                        return clazz(**data)
                except TypeError as error:
                    logger.error(f"Failed to instantiate {clazz.__name__}: {error}")
                    raise
            elif isinstance(data, list):
                # Optional: Handle list of objects if clazz is expected to be a single item
                # This depends on your business logic, returning list as is or mapping it
                return [clazz(**item) if isinstance(item, dict) else item for item in data]

        return data
