import pytest

from cinema_system.viewer import ViewerService


def test_register_and_issue_ticket() -> None:
    vs = ViewerService()
    vs.register_viewer("S101", "Іван Петренко", "D12")
    t = vs.issue_ticket("S101", "Іван Петренко")
    assert "S101" in t.get_ticket_info()
    assert "D12" in t.get_ticket_info()


def test_issue_ticket_without_registration_raises() -> None:
    vs = ViewerService()
    with pytest.raises(ValueError):
        vs.issue_ticket("S101", "Іван Петренко")


def test_ticket_status_flow() -> None:
    vs = ViewerService()
    vs.register_viewer("S101", "Іван Петренко", "D12")
    t = vs.issue_ticket("S101", "Іван Петренко")

    assert "Valid" in t.get_status()
    t.mark_used()
    assert "Used" in t.get_status()

    with pytest.raises(ValueError):
        t.refund()
