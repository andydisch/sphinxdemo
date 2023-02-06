# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from enum import Enum


class CustomerStatus(Enum):
    """This is an enumeration class to represent the customer status.

    This is the body of the docstring description.

    """

    PREMIUM = "premium"
    STANDARD = "standard"


@dataclass
class BillItem:
    """Class to represent a bill item with price and quantity.

    Args:
        price: price of the item.
        quantity: item quantity.

    """

    price: int
    quantity: int = 1

    @property
    def total(self) -> int:
        """Returns the total amount for the bill item.

        Returns:
            The total amount of the bill.

        """
        return self.price * self.quantity


@dataclass
class Customer:
    """Class to represent a customer with name, bills and status.

    Args:
        name: Name of the customer.
        bills: List of all bills of the customer.
        status: Current customer status.

    """

    name: str
    bills: list[BillItem] = field(default_factory=list)
    status: CustomerStatus = CustomerStatus.PREMIUM

    @property
    def open_bills(self) -> int:
        """Returns the total amount of all open bills.

        Returns:
            The total amount of all open bills.

        """
        return sum(item.total for item in self.bills)

    def upgrade(self) -> None:
        """Upgrades customer status to premium.

        Returns:
            Upgrades the customer status.

        """
        self.status = CustomerStatus.PREMIUM
