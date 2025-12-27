from cinema_system.screening import Screening


def test_screening_methods() -> None:
    s = Screening("S101", "Interstellar", "18:30", "2", "On Time")
    assert "S101" in s.get_screening_info()
    assert "18:30" in s.get_schedule()
    assert "On Time" in s.get_status()
