from __future__ import annotations

from screening import Screening
from viewer import ViewerService


def demo() -> None:
    screening = Screening("S101", "Avatar 3", "21:00", "5", "Postponed")


    viewers = ViewerService()

    print(screening.get_screening_info())
    print(screening.get_schedule())
    print(screening.get_status())
    print()

    viewers.register_viewer("S101", "Іван Петренко", "D12")
    ticket = viewers.issue_ticket("S101", "Іван Петренко")

    print("Список глядачів:", viewers.list_viewers("S101"))
    print(ticket.get_ticket_info())
    print(ticket.get_status())

    ticket.mark_used()
    print(ticket.get_status())
