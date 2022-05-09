"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime

if TYPE_CHECKING:
    from ...tl.types import TypeBotCommand, TypeDataJSON


class AnswerWebhookJSONQueryRequest(TLRequest):
    CONSTRUCTOR_ID = 0xE6213F4D
    SUBCLASS_OF_ID = 0xF5B399AC

    def __init__(self, query_id: int, data: "TypeDataJSON"):
        """
        :returns Bool: This type has no constructors.
        """
        self.query_id = query_id
        self.data = data

    def to_dict(self):
        return {
            "_": "AnswerWebhookJSONQueryRequest",
            "query_id": self.query_id,
            "data": self.data.to_dict()
            if isinstance(self.data, TLObject)
            else self.data,
        }

    def _bytes(self):
        return b"".join(
            (
                b"M?!\xe6",
                struct.pack("<q", self.query_id),
                self.data._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _query_id = reader.read_long()
        _data = reader.tgread_object()
        return cls(query_id=_query_id, data=_data)


class SendCustomRequestRequest(TLRequest):
    CONSTRUCTOR_ID = 0xAA2769ED
    SUBCLASS_OF_ID = 0xAD0352E8

    def __init__(self, custom_method: str, params: "TypeDataJSON"):
        """
        :returns DataJSON: Instance of DataJSON.
        """
        self.custom_method = custom_method
        self.params = params

    def to_dict(self):
        return {
            "_": "SendCustomRequestRequest",
            "custom_method": self.custom_method,
            "params": self.params.to_dict()
            if isinstance(self.params, TLObject)
            else self.params,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xedi'\xaa",
                self.serialize_bytes(self.custom_method),
                self.params._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _custom_method = reader.tgread_string()
        _params = reader.tgread_object()
        return cls(custom_method=_custom_method, params=_params)


class SetBotCommandsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x805D46F6
    SUBCLASS_OF_ID = 0xF5B399AC

    def __init__(self, commands: List["TypeBotCommand"]):
        """
        :returns Bool: This type has no constructors.
        """
        self.commands = commands

    def to_dict(self):
        return {
            "_": "SetBotCommandsRequest",
            "commands": []
            if self.commands is None
            else [x.to_dict() if isinstance(x, TLObject) else x for x in self.commands],
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xf6F]\x80",
                b"\x15\xc4\xb5\x1c",
                struct.pack("<i", len(self.commands)),
                b"".join(x._bytes() for x in self.commands),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _commands = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _commands.append(_x)

        return cls(commands=_commands)
