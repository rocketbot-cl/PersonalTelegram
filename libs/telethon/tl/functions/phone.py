"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime

if TYPE_CHECKING:
    from ...tl.types import (
        TypeDataJSON,
        TypeInputGroupCall,
        TypeInputPeer,
        TypeInputPhoneCall,
        TypeInputUser,
        TypePhoneCallDiscardReason,
        TypePhoneCallProtocol,
    )


class AcceptCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3BD2B4A0
    SUBCLASS_OF_ID = 0xD48AFE4F

    def __init__(
        self, peer: "TypeInputPhoneCall", g_b: bytes, protocol: "TypePhoneCallProtocol"
    ):
        """
        :returns phone.PhoneCall: Instance of PhoneCall.
        """
        self.peer = peer
        self.g_b = g_b
        self.protocol = protocol

    def to_dict(self):
        return {
            "_": "AcceptCallRequest",
            "peer": self.peer.to_dict()
            if isinstance(self.peer, TLObject)
            else self.peer,
            "g_b": self.g_b,
            "protocol": self.protocol.to_dict()
            if isinstance(self.protocol, TLObject)
            else self.protocol,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xa0\xb4\xd2;",
                self.peer._bytes(),
                self.serialize_bytes(self.g_b),
                self.protocol._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _g_b = reader.tgread_bytes()
        _protocol = reader.tgread_object()
        return cls(peer=_peer, g_b=_g_b, protocol=_protocol)


class CheckGroupCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0xB74A7BEA
    SUBCLASS_OF_ID = 0xF5B399AC

    def __init__(self, call: "TypeInputGroupCall", source: int):
        """
        :returns Bool: This type has no constructors.
        """
        self.call = call
        self.source = source

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)

    def to_dict(self):
        return {
            "_": "CheckGroupCallRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
            "source": self.source,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xea{J\xb7",
                self.call._bytes(),
                struct.pack("<i", self.source),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _call = reader.tgread_object()
        _source = reader.read_int()
        return cls(call=_call, source=_source)


class ConfirmCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0x2EFE1722
    SUBCLASS_OF_ID = 0xD48AFE4F

    def __init__(
        self,
        peer: "TypeInputPhoneCall",
        g_a: bytes,
        key_fingerprint: int,
        protocol: "TypePhoneCallProtocol",
    ):
        """
        :returns phone.PhoneCall: Instance of PhoneCall.
        """
        self.peer = peer
        self.g_a = g_a
        self.key_fingerprint = key_fingerprint
        self.protocol = protocol

    def to_dict(self):
        return {
            "_": "ConfirmCallRequest",
            "peer": self.peer.to_dict()
            if isinstance(self.peer, TLObject)
            else self.peer,
            "g_a": self.g_a,
            "key_fingerprint": self.key_fingerprint,
            "protocol": self.protocol.to_dict()
            if isinstance(self.protocol, TLObject)
            else self.protocol,
        }

    def _bytes(self):
        return b"".join(
            (
                b'"\x17\xfe.',
                self.peer._bytes(),
                self.serialize_bytes(self.g_a),
                struct.pack("<q", self.key_fingerprint),
                self.protocol._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _g_a = reader.tgread_bytes()
        _key_fingerprint = reader.read_long()
        _protocol = reader.tgread_object()
        return cls(
            peer=_peer, g_a=_g_a, key_fingerprint=_key_fingerprint, protocol=_protocol
        )


class CreateGroupCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0xBD3DABE0
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(self, peer: "TypeInputPeer", random_id: int = None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.random_id = (
            random_id
            if random_id is not None
            else int.from_bytes(os.urandom(4), "big", signed=True)
        )

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            "_": "CreateGroupCallRequest",
            "peer": self.peer.to_dict()
            if isinstance(self.peer, TLObject)
            else self.peer,
            "random_id": self.random_id,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xe0\xab=\xbd",
                self.peer._bytes(),
                struct.pack("<i", self.random_id),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _random_id = reader.read_int()
        return cls(peer=_peer, random_id=_random_id)


class DiscardCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0xB2CBC1C0
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(
        self,
        peer: "TypeInputPhoneCall",
        duration: int,
        reason: "TypePhoneCallDiscardReason",
        connection_id: int,
        video: Optional[bool] = None,
    ):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.duration = duration
        self.reason = reason
        self.connection_id = connection_id
        self.video = video

    def to_dict(self):
        return {
            "_": "DiscardCallRequest",
            "peer": self.peer.to_dict()
            if isinstance(self.peer, TLObject)
            else self.peer,
            "duration": self.duration,
            "reason": self.reason.to_dict()
            if isinstance(self.reason, TLObject)
            else self.reason,
            "connection_id": self.connection_id,
            "video": self.video,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xc0\xc1\xcb\xb2",
                struct.pack(
                    "<I", (0 if self.video is None or self.video is False else 1)
                ),
                self.peer._bytes(),
                struct.pack("<i", self.duration),
                self.reason._bytes(),
                struct.pack("<q", self.connection_id),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _video = bool(flags & 1)
        _peer = reader.tgread_object()
        _duration = reader.read_int()
        _reason = reader.tgread_object()
        _connection_id = reader.read_long()
        return cls(
            peer=_peer,
            duration=_duration,
            reason=_reason,
            connection_id=_connection_id,
            video=_video,
        )


class DiscardGroupCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7A777135
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(self, call: "TypeInputGroupCall"):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.call = call

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)

    def to_dict(self):
        return {
            "_": "DiscardGroupCallRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
        }

    def _bytes(self):
        return b"".join(
            (
                b"5qwz",
                self.call._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _call = reader.tgread_object()
        return cls(call=_call)


class EditGroupCallParticipantRequest(TLRequest):
    CONSTRUCTOR_ID = 0xD975EB80
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(
        self,
        call: "TypeInputGroupCall",
        participant: "TypeInputPeer",
        muted: Optional[bool] = None,
        volume: Optional[int] = None,
        raise_hand: Optional[bool] = None,
    ):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.call = call
        self.participant = participant
        self.muted = muted
        self.volume = volume
        self.raise_hand = raise_hand

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)
        self.participant = utils.get_input_peer(
            await client.get_input_entity(self.participant)
        )

    def to_dict(self):
        return {
            "_": "EditGroupCallParticipantRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
            "participant": self.participant.to_dict()
            if isinstance(self.participant, TLObject)
            else self.participant,
            "muted": self.muted,
            "volume": self.volume,
            "raise_hand": self.raise_hand,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\x80\xebu\xd9",
                struct.pack(
                    "<I",
                    (0 if self.muted is None or self.muted is False else 1)
                    | (0 if self.volume is None or self.volume is False else 2)
                    | (0 if self.raise_hand is None else 4),
                ),
                self.call._bytes(),
                self.participant._bytes(),
                b""
                if self.volume is None or self.volume is False
                else (struct.pack("<i", self.volume)),
                b""
                if self.raise_hand is None
                else (b"\xb5ur\x99" if self.raise_hand else b"7\x97y\xbc"),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _muted = bool(flags & 1)
        _call = reader.tgread_object()
        _participant = reader.tgread_object()
        if flags & 2:
            _volume = reader.read_int()
        else:
            _volume = None
        if flags & 4:
            _raise_hand = reader.tgread_bool()
        else:
            _raise_hand = None
        return cls(
            call=_call,
            participant=_participant,
            muted=_muted,
            volume=_volume,
            raise_hand=_raise_hand,
        )


class EditGroupCallTitleRequest(TLRequest):
    CONSTRUCTOR_ID = 0x1CA6AC0A
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(self, call: "TypeInputGroupCall", title: str):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.call = call
        self.title = title

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)

    def to_dict(self):
        return {
            "_": "EditGroupCallTitleRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
            "title": self.title,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\n\xac\xa6\x1c",
                self.call._bytes(),
                self.serialize_bytes(self.title),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _call = reader.tgread_object()
        _title = reader.tgread_string()
        return cls(call=_call, title=_title)


class ExportGroupCallInviteRequest(TLRequest):
    CONSTRUCTOR_ID = 0xE6AA647F
    SUBCLASS_OF_ID = 0x3B3BFE8F

    def __init__(
        self, call: "TypeInputGroupCall", can_self_unmute: Optional[bool] = None
    ):
        """
        :returns phone.ExportedGroupCallInvite: Instance of ExportedGroupCallInvite.
        """
        self.call = call
        self.can_self_unmute = can_self_unmute

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)

    def to_dict(self):
        return {
            "_": "ExportGroupCallInviteRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
            "can_self_unmute": self.can_self_unmute,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\x7fd\xaa\xe6",
                struct.pack(
                    "<I",
                    (
                        0
                        if self.can_self_unmute is None or self.can_self_unmute is False
                        else 1
                    ),
                ),
                self.call._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _can_self_unmute = bool(flags & 1)
        _call = reader.tgread_object()
        return cls(call=_call, can_self_unmute=_can_self_unmute)


class GetCallConfigRequest(TLRequest):
    CONSTRUCTOR_ID = 0x55451FA9
    SUBCLASS_OF_ID = 0xAD0352E8

    def to_dict(self):
        return {"_": "GetCallConfigRequest"}

    def _bytes(self):
        return b"".join((b"\xa9\x1fEU",))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class GetGroupCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0xC7CB017
    SUBCLASS_OF_ID = 0x304116BE

    def __init__(self, call: "TypeInputGroupCall"):
        """
        :returns phone.GroupCall: Instance of GroupCall.
        """
        self.call = call

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)

    def to_dict(self):
        return {
            "_": "GetGroupCallRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\x17\xb0|\x0c",
                self.call._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _call = reader.tgread_object()
        return cls(call=_call)


class GetGroupCallJoinAsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xEF7C213A
    SUBCLASS_OF_ID = 0xB4B770FB

    def __init__(self, peer: "TypeInputPeer"):
        """
        :returns phone.JoinAsPeers: Instance of JoinAsPeers.
        """
        self.peer = peer

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            "_": "GetGroupCallJoinAsRequest",
            "peer": self.peer.to_dict()
            if isinstance(self.peer, TLObject)
            else self.peer,
        }

    def _bytes(self):
        return b"".join(
            (
                b":!|\xef",
                self.peer._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        return cls(peer=_peer)


class GetGroupParticipantsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xC558D8AB
    SUBCLASS_OF_ID = 0x72D304F4

    def __init__(
        self,
        call: "TypeInputGroupCall",
        ids: List["TypeInputPeer"],
        sources: List[int],
        offset: str,
        limit: int,
    ):
        """
        :returns phone.GroupParticipants: Instance of GroupParticipants.
        """
        self.call = call
        self.ids = ids
        self.sources = sources
        self.offset = offset
        self.limit = limit

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)
        _tmp = []
        for _x in self.ids:
            _tmp.append(utils.get_input_peer(await client.get_input_entity(_x)))

        self.ids = _tmp

    def to_dict(self):
        return {
            "_": "GetGroupParticipantsRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
            "ids": []
            if self.ids is None
            else [x.to_dict() if isinstance(x, TLObject) else x for x in self.ids],
            "sources": [] if self.sources is None else self.sources[:],
            "offset": self.offset,
            "limit": self.limit,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xab\xd8X\xc5",
                self.call._bytes(),
                b"\x15\xc4\xb5\x1c",
                struct.pack("<i", len(self.ids)),
                b"".join(x._bytes() for x in self.ids),
                b"\x15\xc4\xb5\x1c",
                struct.pack("<i", len(self.sources)),
                b"".join(struct.pack("<i", x) for x in self.sources),
                self.serialize_bytes(self.offset),
                struct.pack("<i", self.limit),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _call = reader.tgread_object()
        reader.read_int()
        _ids = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _ids.append(_x)

        reader.read_int()
        _sources = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _sources.append(_x)

        _offset = reader.tgread_string()
        _limit = reader.read_int()
        return cls(call=_call, ids=_ids, sources=_sources, offset=_offset, limit=_limit)


class InviteToGroupCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7B393160
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(self, call: "TypeInputGroupCall", users: List["TypeInputUser"]):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.call = call
        self.users = users

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)
        _tmp = []
        for _x in self.users:
            _tmp.append(utils.get_input_user(await client.get_input_entity(_x)))

        self.users = _tmp

    def to_dict(self):
        return {
            "_": "InviteToGroupCallRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
            "users": []
            if self.users is None
            else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users],
        }

    def _bytes(self):
        return b"".join(
            (
                b"`19{",
                self.call._bytes(),
                b"\x15\xc4\xb5\x1c",
                struct.pack("<i", len(self.users)),
                b"".join(x._bytes() for x in self.users),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _call = reader.tgread_object()
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(call=_call, users=_users)


class JoinGroupCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0xB132FF7B
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(
        self,
        call: "TypeInputGroupCall",
        join_as: "TypeInputPeer",
        params: "TypeDataJSON",
        muted: Optional[bool] = None,
        invite_hash: Optional[str] = None,
    ):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.call = call
        self.join_as = join_as
        self.params = params
        self.muted = muted
        self.invite_hash = invite_hash

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)
        self.join_as = utils.get_input_peer(await client.get_input_entity(self.join_as))

    def to_dict(self):
        return {
            "_": "JoinGroupCallRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
            "join_as": self.join_as.to_dict()
            if isinstance(self.join_as, TLObject)
            else self.join_as,
            "params": self.params.to_dict()
            if isinstance(self.params, TLObject)
            else self.params,
            "muted": self.muted,
            "invite_hash": self.invite_hash,
        }

    def _bytes(self):
        return b"".join(
            (
                b"{\xff2\xb1",
                struct.pack(
                    "<I",
                    (0 if self.muted is None or self.muted is False else 1)
                    | (
                        0
                        if self.invite_hash is None or self.invite_hash is False
                        else 2
                    ),
                ),
                self.call._bytes(),
                self.join_as._bytes(),
                b""
                if self.invite_hash is None or self.invite_hash is False
                else (self.serialize_bytes(self.invite_hash)),
                self.params._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _muted = bool(flags & 1)
        _call = reader.tgread_object()
        _join_as = reader.tgread_object()
        if flags & 2:
            _invite_hash = reader.tgread_string()
        else:
            _invite_hash = None
        _params = reader.tgread_object()
        return cls(
            call=_call,
            join_as=_join_as,
            params=_params,
            muted=_muted,
            invite_hash=_invite_hash,
        )


class LeaveGroupCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0x500377F9
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(self, call: "TypeInputGroupCall", source: int):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.call = call
        self.source = source

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)

    def to_dict(self):
        return {
            "_": "LeaveGroupCallRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
            "source": self.source,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xf9w\x03P",
                self.call._bytes(),
                struct.pack("<i", self.source),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _call = reader.tgread_object()
        _source = reader.read_int()
        return cls(call=_call, source=_source)


class ReceivedCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0x17D54F61
    SUBCLASS_OF_ID = 0xF5B399AC

    def __init__(self, peer: "TypeInputPhoneCall"):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer

    def to_dict(self):
        return {
            "_": "ReceivedCallRequest",
            "peer": self.peer.to_dict()
            if isinstance(self.peer, TLObject)
            else self.peer,
        }

    def _bytes(self):
        return b"".join(
            (
                b"aO\xd5\x17",
                self.peer._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        return cls(peer=_peer)


class RequestCallRequest(TLRequest):
    CONSTRUCTOR_ID = 0x42FF96ED
    SUBCLASS_OF_ID = 0xD48AFE4F

    def __init__(
        self,
        user_id: "TypeInputUser",
        g_a_hash: bytes,
        protocol: "TypePhoneCallProtocol",
        video: Optional[bool] = None,
        random_id: int = None,
    ):
        """
        :returns phone.PhoneCall: Instance of PhoneCall.
        """
        self.user_id = user_id
        self.g_a_hash = g_a_hash
        self.protocol = protocol
        self.video = video
        self.random_id = (
            random_id
            if random_id is not None
            else int.from_bytes(os.urandom(4), "big", signed=True)
        )

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            "_": "RequestCallRequest",
            "user_id": self.user_id.to_dict()
            if isinstance(self.user_id, TLObject)
            else self.user_id,
            "g_a_hash": self.g_a_hash,
            "protocol": self.protocol.to_dict()
            if isinstance(self.protocol, TLObject)
            else self.protocol,
            "video": self.video,
            "random_id": self.random_id,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xed\x96\xffB",
                struct.pack(
                    "<I", (0 if self.video is None or self.video is False else 1)
                ),
                self.user_id._bytes(),
                struct.pack("<i", self.random_id),
                self.serialize_bytes(self.g_a_hash),
                self.protocol._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _video = bool(flags & 1)
        _user_id = reader.tgread_object()
        _random_id = reader.read_int()
        _g_a_hash = reader.tgread_bytes()
        _protocol = reader.tgread_object()
        return cls(
            user_id=_user_id,
            g_a_hash=_g_a_hash,
            protocol=_protocol,
            video=_video,
            random_id=_random_id,
        )


class SaveCallDebugRequest(TLRequest):
    CONSTRUCTOR_ID = 0x277ADD7E
    SUBCLASS_OF_ID = 0xF5B399AC

    def __init__(self, peer: "TypeInputPhoneCall", debug: "TypeDataJSON"):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.debug = debug

    def to_dict(self):
        return {
            "_": "SaveCallDebugRequest",
            "peer": self.peer.to_dict()
            if isinstance(self.peer, TLObject)
            else self.peer,
            "debug": self.debug.to_dict()
            if isinstance(self.debug, TLObject)
            else self.debug,
        }

    def _bytes(self):
        return b"".join(
            (
                b"~\xddz'",
                self.peer._bytes(),
                self.debug._bytes(),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _debug = reader.tgread_object()
        return cls(peer=_peer, debug=_debug)


class SendSignalingDataRequest(TLRequest):
    CONSTRUCTOR_ID = 0xFF7A9383
    SUBCLASS_OF_ID = 0xF5B399AC

    def __init__(self, peer: "TypeInputPhoneCall", data: bytes):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.data = data

    def to_dict(self):
        return {
            "_": "SendSignalingDataRequest",
            "peer": self.peer.to_dict()
            if isinstance(self.peer, TLObject)
            else self.peer,
            "data": self.data,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\x83\x93z\xff",
                self.peer._bytes(),
                self.serialize_bytes(self.data),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _data = reader.tgread_bytes()
        return cls(peer=_peer, data=_data)


class SetCallRatingRequest(TLRequest):
    CONSTRUCTOR_ID = 0x59EAD627
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(
        self,
        peer: "TypeInputPhoneCall",
        rating: int,
        comment: str,
        user_initiative: Optional[bool] = None,
    ):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.rating = rating
        self.comment = comment
        self.user_initiative = user_initiative

    def to_dict(self):
        return {
            "_": "SetCallRatingRequest",
            "peer": self.peer.to_dict()
            if isinstance(self.peer, TLObject)
            else self.peer,
            "rating": self.rating,
            "comment": self.comment,
            "user_initiative": self.user_initiative,
        }

    def _bytes(self):
        return b"".join(
            (
                b"'\xd6\xeaY",
                struct.pack(
                    "<I",
                    (
                        0
                        if self.user_initiative is None or self.user_initiative is False
                        else 1
                    ),
                ),
                self.peer._bytes(),
                struct.pack("<i", self.rating),
                self.serialize_bytes(self.comment),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _user_initiative = bool(flags & 1)
        _peer = reader.tgread_object()
        _rating = reader.read_int()
        _comment = reader.tgread_string()
        return cls(
            peer=_peer,
            rating=_rating,
            comment=_comment,
            user_initiative=_user_initiative,
        )


class ToggleGroupCallRecordRequest(TLRequest):
    CONSTRUCTOR_ID = 0xC02A66D7
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(
        self,
        call: "TypeInputGroupCall",
        start: Optional[bool] = None,
        title: Optional[str] = None,
    ):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.call = call
        self.start = start
        self.title = title

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)

    def to_dict(self):
        return {
            "_": "ToggleGroupCallRecordRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
            "start": self.start,
            "title": self.title,
        }

    def _bytes(self):
        return b"".join(
            (
                b"\xd7f*\xc0",
                struct.pack(
                    "<I",
                    (0 if self.start is None or self.start is False else 1)
                    | (0 if self.title is None or self.title is False else 2),
                ),
                self.call._bytes(),
                b""
                if self.title is None or self.title is False
                else (self.serialize_bytes(self.title)),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _start = bool(flags & 1)
        _call = reader.tgread_object()
        if flags & 2:
            _title = reader.tgread_string()
        else:
            _title = None
        return cls(call=_call, start=_start, title=_title)


class ToggleGroupCallSettingsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x74BBB43D
    SUBCLASS_OF_ID = 0x8AF52AAC

    def __init__(
        self,
        call: "TypeInputGroupCall",
        reset_invite_hash: Optional[bool] = None,
        join_muted: Optional[bool] = None,
    ):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.call = call
        self.reset_invite_hash = reset_invite_hash
        self.join_muted = join_muted

    async def resolve(self, client, utils):
        self.call = utils.get_input_group_call(self.call)

    def to_dict(self):
        return {
            "_": "ToggleGroupCallSettingsRequest",
            "call": self.call.to_dict()
            if isinstance(self.call, TLObject)
            else self.call,
            "reset_invite_hash": self.reset_invite_hash,
            "join_muted": self.join_muted,
        }

    def _bytes(self):
        return b"".join(
            (
                b"=\xb4\xbbt",
                struct.pack(
                    "<I",
                    (
                        0
                        if self.reset_invite_hash is None
                        or self.reset_invite_hash is False
                        else 2
                    )
                    | (0 if self.join_muted is None else 1),
                ),
                self.call._bytes(),
                b""
                if self.join_muted is None
                else (b"\xb5ur\x99" if self.join_muted else b"7\x97y\xbc"),
            )
        )

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _reset_invite_hash = bool(flags & 2)
        _call = reader.tgread_object()
        if flags & 1:
            _join_muted = reader.tgread_bool()
        else:
            _join_muted = None
        return cls(
            call=_call, reset_invite_hash=_reset_invite_hash, join_muted=_join_muted
        )
