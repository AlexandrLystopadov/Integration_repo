from __future__ import annotations

from dataclasses import dataclass, field

from  cinema_system.interfaces import IViewer, ITicket
from cinema_system.ticket import Ticket


@dataclass
class ViewerService(IViewer):
    _viewers: dict[str, list[dict]] = field(default_factory=dict)

    def register_viewer(self, screening_id: str, full_name: str, seat: str) -> None:
        viewers = self._viewers.setdefault(screening_id, [])
        if any(v["full_name"] == full_name for v in viewers):
            raise ValueError("Цей глядач вже зареєстрований на даний сеанс.")
        viewers.append({"full_name": full_name, "seat": seat})

    def issue_ticket(self, screening_id: str, full_name: str) -> ITicket:
        viewers = self._viewers.get(screening_id, [])
        viewer = next((v for v in viewers if v["full_name"] == full_name), None)
        if viewer is None:
            raise ValueError("Глядач не зареєстрований на цей сеанс.")
        return Ticket(screening_id=screening_id, full_name=full_name, seat=viewer["seat"])

    def list_viewers(self, screening_id: str) -> list[dict]:
        return list(self._viewers.get(screening_id, []))
