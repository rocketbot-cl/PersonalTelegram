"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime


class FileGif(TLObject):
    CONSTRUCTOR_ID = 0xCAE1AADF
    SUBCLASS_OF_ID = 0xF3A1E6F3

    def to_dict(self):
        return {"_": "FileGif"}

    def _bytes(self):
        return b"".join((b"\xdf\xaa\xe1\xca",))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class FileJpeg(TLObject):
    CONSTRUCTOR_ID = 0x7EFE0E
    SUBCLASS_OF_ID = 0xF3A1E6F3

    def to_dict(self):
        return {"_": "FileJpeg"}

    def _bytes(self):
        return b"".join((b"\x0e\xfe~\x00",))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class FileMov(TLObject):
    CONSTRUCTOR_ID = 0x4B09EBBC
    SUBCLASS_OF_ID = 0xF3A1E6F3

    def to_dict(self):
        return {"_": "FileMov"}

    def _bytes(self):
        return b"".join((b"\xbc\xeb\tK",))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class FileMp3(TLObject):
    CONSTRUCTOR_ID = 0x528A0677
    SUBCLASS_OF_ID = 0xF3A1E6F3

    def to_dict(self):
        return {"_": "FileMp3"}

    def _bytes(self):
        return b"".join((b"w\x06\x8aR",))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class FileMp4(TLObject):
    CONSTRUCTOR_ID = 0xB3CEA0E4
    SUBCLASS_OF_ID = 0xF3A1E6F3

    def to_dict(self):
        return {"_": "FileMp4"}

    def _bytes(self):
        return b"".join((b"\xe4\xa0\xce\xb3",))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class FilePartial(TLObject):
    CONSTRUCTOR_ID = 0x40BC6F52
    SUBCLASS_OF_ID = 0xF3A1E6F3

    def to_dict(self):
        return {"_": "FilePartial"}

    def _bytes(self):
        return b"".join((b"Ro\xbc@",))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class FilePdf(TLObject):
    CONSTRUCTOR_ID = 0xAE1E508D
    SUBCLASS_OF_ID = 0xF3A1E6F3

    def to_dict(self):
        return {"_": "FilePdf"}

    def _bytes(self):
        return b"".join((b"\x8dP\x1e\xae",))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class FilePng(TLObject):
    CONSTRUCTOR_ID = 0xA4F63C0
    SUBCLASS_OF_ID = 0xF3A1E6F3

    def to_dict(self):
        return {"_": "FilePng"}

    def _bytes(self):
        return b"".join((b"\xc0cO\n",))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class FileUnknown(TLObject):
    CONSTRUCTOR_ID = 0xAA963B05
    SUBCLASS_OF_ID = 0xF3A1E6F3

    def to_dict(self):
        return {"_": "FileUnknown"}

    def _bytes(self):
        return b"".join((b"\x05;\x96\xaa",))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class FileWebp(TLObject):
    CONSTRUCTOR_ID = 0x1081464C
    SUBCLASS_OF_ID = 0xF3A1E6F3

    def to_dict(self):
        return {"_": "FileWebp"}

    def _bytes(self):
        return b"".join((b"LF\x81\x10",))

    @classmethod
    def from_reader(cls, reader):
        return cls()
