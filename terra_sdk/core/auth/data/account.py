"""Data objects pertaining to accounts."""

from __future__ import annotations


import attr

from terra_sdk.core import AccAddress, Coins
from terra_sdk.util.json import JSONSerializable

from .public_key import PublicKey

__all__ = ["Account"]


@attr.s
class Account(JSONSerializable):
    """Stores information about an account."""

    address: AccAddress = attr.ib()
    """"""

    coins: Coins = attr.ib(converter=Coins)
    """"""

    public_key: PublicKey = attr.ib()
    """"""

    account_number: int = attr.ib(converter=int)
    """"""

    sequence: int = attr.ib(converter=int)
    """"""

    def to_data(self) -> dict:
        return {
            "type": "core/Account",
            "value": {
                "address": self.address,
                "coins": self.coins.to_data(),
                "public_key": self.public_key.to_data(),
                "account_number": str(self.account_number),
                "sequence": str(self.sequence),
            },
        }

    @classmethod
    def from_data(cls, data: dict) -> Account:
        data = data["value"]
        return cls(
            address=data["address"],
            coins=Coins.from_data(data["coins"]),
            public_key=PublicKey.from_data(data["public_key"]),
            account_number=data["account_number"],
            sequence=data["sequence"],
        )

