import pytest


@pytest.mark.parametrize("HDL, expected", [
        (65, "Normal"),
        (45, "Borderline Low"),
        (35, "Low")
        ])
def test_analyze_HDL(HDL, expected):
    from blood_tests import analyze_HDL
    answer = analyze_HDL(HDL)
    assert answer == expected
