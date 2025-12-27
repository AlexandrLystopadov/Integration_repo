from __future__ import annotations

from abc import ABC, abstractmethod


class IScreening(ABC):
    """Інтерфейс для управління сеансом."""

    @abstractmethod
    def get_screening_info(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_schedule(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_status(self) -> str:
        raise NotImplementedError


class IViewer(ABC):
    """Інтерфейс для реєстрації глядачів і видачі квитків."""

    @abstractmethod
    def register_viewer(self, screening_id: str, full_name: str, seat: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def issue_ticket(self, screening_id: str, full_name: str):
        raise NotImplementedError

    @abstractmethod
    def list_viewers(self, screening_id: str) -> list[dict]:
        raise NotImplementedError


class ITicket(ABC):
    """Інтерфейс для квитка: маркування та відстеження статусу."""

    @abstractmethod
    def get_ticket_info(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def mark_used(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def refund(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_status(self) -> str:
        raise NotImplementedError
