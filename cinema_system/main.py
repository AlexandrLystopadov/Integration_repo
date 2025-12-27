from __future__ import annotations

from screening import Screening


def demo() -> None:
    screening = Screening("S101", "Interstellar", "18:30", "2", "On Time")

    print(screening.get_screening_info())
    print(screening.get_schedule())
    print(screening.get_status())
