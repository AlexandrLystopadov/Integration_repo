from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4

from cinema_system.interfaces import ITicket


@dataclass(slots=True)
class Ticket(ITicket):
    screening_id: str
    full_name: str
    seat: str
    ticket_id: str = field(default_factory=lambda: uuid4().hex[:10])
    status: str = "Valid"

    def get_ticket_info(self) -> str:
        return (
            f"Квиток {self.ticket_id}: сеанс {self.screening_id}, глядач {self.full_name}, місце {self.seat}"
        )

    def mark_used(self) -> None:
        if self.status != "Valid":
            raise ValueError("Квиток не можна використати: він не у статусі Valid.")
        self.status = "Used"

    def refund(self) -> None:
        if self.status == "Used":
            raise ValueError("Неможливо повернути використаний квиток.")
        self.status = "Refunded"

    def get_status(self) -> str:
        return f"Статус квитка: {self.status}"
