"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime

if TYPE_CHECKING:
    from ...tl.types import TypeInputPaymentCredentials, TypePaymentRequestedInfo


class ClearSavedInfoRequest(TLRequest):
    CONSTRUCTOR_ID = 0xD83D70C1
    SUBCLASS_OF_ID = 0xF5B399AC

    def __init__(self, credentials: Optional[bool] = None, info: Optional[bool] = None):
        """
        :returns Bool: This type has no constructors.
        """
        self.credentials = credentials
        self.info = info

    def to_dict(self):
        return {
            "_": "ClearSavedInfoRequest",
            "credentials": self.credentials,
            "info": self.info,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xc1p=\xd8",
                struct.pack(
                    "<I",
                    (0 if self.credentials is None or self.credentials is False else 1)
                    | (0 if self.info is None or self.info is False else 2),
                ),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _credentials = bool(flags & 1)
        _info = bool(flags & 2)
        return cls(credentials=_credentials, info=_info)


class GetBankCardDataRequest(TLRequest):
    CONSTRUCTOR_ID = 0x2E79D779
    SUBCLASS_OF_ID = 0x8C6DD68B

    def __init__(self, number: str):
        """
        :returns payments.BankCardData: Instance of BankCardData.
        """
        self.number = number

    def to_dict(self):
        return {"_": "GetBankCardDataRequest", "number": self.number}

    def _bytes(self):
        return b"".join(
            (
                b"y\xd7y.",
                self.serialize_bytes(self.number),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _number = reader.tgread_string()
        return cls(number=_number)


class GetPaymentFormRequest(TLRequest):
    CONSTRUCTOR_ID = 0x99F09745
    SUBCLASS_OF_ID = 0xA0483F19

    def __init__(self, msg_id: int):
        """
        :returns payments.PaymentForm: Instance of PaymentForm.
        """
        self.msg_id = msg_id

    def to_dict(self):
        return {"_": "GetPaymentFormRequest", "msg_id": self.msg_id}

    def _bytes(self):
        return b"".join(
            (
                b"E\x97\xf0\x99",
                struct.pack("<i", self.msg_id),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _msg_id = reader.read_int()
        return cls(msg_id=_msg_id)


class GetPaymentReceiptRequest(TLRequest):
    CONSTRUCTOR_ID = 0xA092A980
    SUBCLASS_OF_ID = 0x590093C9

    def __init__(self, msg_id: int):
        """
        :returns payments.PaymentReceipt: Instance of PaymentReceipt.
        """
        self.msg_id = msg_id

    def to_dict(self):
        return {"_": "GetPaymentReceiptRequest", "msg_id": self.msg_id}

    def _bytes(self):
        return b"".join(
            (
                b"\x80\xa9\x92\xa0",
                struct.pack("<i", self.msg_id),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _msg_id = reader.read_int()
        return cls(msg_id=_msg_id)


class GetSavedInfoRequest(TLRequest):
    CONSTRUCTOR_ID = 0x227D824B
    SUBCLASS_OF_ID = 0xAD3CF146

    def to_dict(self):
        return {"_": "GetSavedInfoRequest"}

    def _bytes(self):
        return b"".join((b'K\x82}"',))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class SendPaymentFormRequest(TLRequest):
    CONSTRUCTOR_ID = 0x2B8879B3
    SUBCLASS_OF_ID = 0x8AE16A9D

    def __init__(
        self,
        msg_id: int,
        credentials: "TypeInputPaymentCredentials",
        requested_info_id: Optional[str] = None,
        shipping_option_id: Optional[str] = None,
    ):
        """
        :returns payments.PaymentResult: Instance of either PaymentResult, PaymentVerificationNeeded.
        """
        self.msg_id = msg_id
        self.credentials = credentials
        self.requested_info_id = requested_info_id
        self.shipping_option_id = shipping_option_id

    def to_dict(self):
        return {
            "_": "SendPaymentFormRequest",
            "msg_id": self.msg_id,
            "credentials": self.credentials.to_dict()
            if isinstance(self.credentials, TLObject)
            else self.credentials,
            "requested_info_id": self.requested_info_id,
            "shipping_option_id": self.shipping_option_id,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xb3y\x88+",
                struct.pack(
                    "<I",
                    (
                        0
                        if self.requested_info_id is None
                        or self.requested_info_id is False
                        else 1
                    )
                    | (
                        0
                        if self.shipping_option_id is None
                        or self.shipping_option_id is False
                        else 2
                    ),
                ),
                struct.pack("<i", self.msg_id),
                b""
                if self.requested_info_id is None or self.requested_info_id is False
                else (self.serialize_bytes(self.requested_info_id)),
                b""
                if self.shipping_option_id is None or self.shipping_option_id is False
                else (self.serialize_bytes(self.shipping_option_id)),
                self.credentials._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _msg_id = reader.read_int()
        if flags & 1:
            _requested_info_id = reader.tgread_string()
        else:
            _requested_info_id = None
        if flags & 2:
            _shipping_option_id = reader.tgread_string()
        else:
            _shipping_option_id = None
        _credentials = reader.tgread_object()
        return cls(
            msg_id=_msg_id,
            credentials=_credentials,
            requested_info_id=_requested_info_id,
            shipping_option_id=_shipping_option_id,
        )


class ValidateRequestedInfoRequest(TLRequest):
    CONSTRUCTOR_ID = 0x770A8E74
    SUBCLASS_OF_ID = 0x8F8044B7

    def __init__(
        self, msg_id: int, info: "TypePaymentRequestedInfo", save: Optional[bool] = None
    ):
        """
        :returns payments.ValidatedRequestedInfo: Instance of ValidatedRequestedInfo.
        """
        self.msg_id = msg_id
        self.info = info
        self.save = save

    def to_dict(self):
        return {
            "_": "ValidateRequestedInfoRequest",
            "msg_id": self.msg_id,
            "info": self.info.to_dict()
            if isinstance(self.info, TLObject)
            else self.info,
            "save": self.save,
        }

    def _bytes(self):
        return b"".join(
            (
                b"t\x8e\nw",
                struct.pack(
                    "<I", (0 if self.save is None or self.save is False else 1)
                ),
                struct.pack("<i", self.msg_id),
                self.info._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _save = bool(flags & 1)
        _msg_id = reader.read_int()
        _info = reader.tgread_object()
        return cls(msg_id=_msg_id, info=_info, save=_save)
