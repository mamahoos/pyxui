from typing import TypedDict
import sys

if sys.version_info >= (3, 11):
    from typing import Self
else:
    Self = "Config"


class ClientDict(TypedDict):
    id        : str
    email     : str
    enable    : bool
    flow      : str
    limitIp   : int
    totalGB   : int
    expiryTime: int
    tgId      : str
    subId     : str


class Client:
    __slots__ = (
        "id",
        "flow",
        "email",
        "enable",
        "limit_ip",
        "total_gb",
        "expiry_time",
        "telegram_id",
        "subscription_id"
    )

    def __init__(
        self,
        id: str,
        email: str,
        enable: bool = True,
        flow: str = "",
        limit_ip: int = 0,
        total_gb: int = 0,
        expiry_time: int = 0,
        telegram_id: str = "",
        subscription_id: str = ""
    ) -> None:
        self.id              = id
        self.email           = email
        self.enable          = enable
        self.flow            = flow
        self.limit_ip        = limit_ip
        self.total_gb        = total_gb
        self.expiry_time     = expiry_time
        self.telegram_id     = telegram_id
        self.subscription_id = subscription_id

    @classmethod
    def from_dict(cls, data: ClientDict) -> Self:
        return cls(
            id              = data.get("id"),
            email           = data.get("email"),
            enable          = data.get("enable", True),
            flow            = data.get("flow", ""),
            limit_ip        = data.get("limitIp", 0),
            total_gb        = data.get("totalGB", 0),
            expiry_time     = data.get("expiryTime", 0),
            telegram_id     = data.get("tgId", ""),
            subscription_id = data.get("subId", "")
        )

    def to_dict(self) -> ClientDict:
        return {
            "id"        : self.id,
            "email"     : self.email,
            "enable"    : self.enable,
            "flow"      : self.flow,
            "limitIp"   : self.limit_ip,
            "totalGB"   : self.total_gb,
            "expiryTime": self.expiry_time,
            "tgId"      : self.telegram_id,
            "subId"     : self.subscription_id
        }
