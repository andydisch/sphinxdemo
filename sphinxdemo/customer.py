# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from enum import Enum


class CustomerStatus(Enum):
    """Enumeration class to represent customer status.

    """

    PREMIUM = "premium"
    STANDARD = "standard"


@dataclass
class BillItem:
    """Class to represent a bill item with price and quantity.

    """

    price: int
    quantity: int = 1

    @property
    def total(self) -> int:
        """Returns the total amount for the bill item.

        """
        return self.price * self.quantity


@dataclass
class Customer:
    """Class to represent a customer with name, bills and status.

    """

    name: str
    bills: list[BillItem] = field(default_factory=list)
    status: CustomerStatus = CustomerStatus.PREMIUM

    @property
    def open_bills(self) -> int:
        """Returns the total amount of all open bills.

        """
        return sum(item.total for item in self.bills)

    def upgrade(self) -> None:
        """Upgrades customer status to premium.
        
        """
        self.status = CustomerStatus.PREMIUM
