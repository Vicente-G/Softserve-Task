import pytest

from ball_clock import clock_mode1, clock_mode2


def test_mode1_correct():
    result = clock_mode1(30)
    days = round(result.cycles / 2, 0)
    assert days == 15


def test_mode1_correct_alt():
    result = clock_mode1(45)
    days = round(result.cycles / 2, 0)
    assert days == 378


def test_mode2_correct():
    result = clock_mode2(30, 325)
    assert result.get_state() == {
        "Min": [],
        "FiveMin": [22, 13, 25, 3, 7],
        "Hour": [6, 12, 17, 4, 15],
        "Main": [
            11,
            5,
            26,
            18,
            2,
            30,
            19,
            8,
            24,
            10,
            29,
            20,
            16,
            21,
            28,
            1,
            23,
            14,
            27,
            9,
        ],
    }


def test_mode1_incorrect():
    with pytest.raises(ValueError):
        clock_mode1(26)


def test_mode2_incorrect():
    with pytest.raises(ValueError):
        clock_mode2(128, 1)
