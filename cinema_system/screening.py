from __future__ import annotations

from dataclasses import dataclass

from interfaces import IScreening


@dataclass(slots=True)
class Screening(IScreening):
    screening_id: str
    movie_title: str
    start_time: str
    hall: str
    status: str = "Scheduled"

    def get_screening_info(self) -> str:
        return (
            f"Сеанс №{self.screening_id}: '{self.movie_title}', зал {self.hall}, початок {self.start_time}"
        )

    def get_schedule(self) -> str:
        return f"Розклад: {self.start_time}"

    def get_status(self) -> str:

        return f"STATUS OF MOVIE: {self.status}"



