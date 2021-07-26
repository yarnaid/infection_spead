import pytest
import Codethuattoan
import sys


@pytest.mark.example1
def test_mode_rungeKutta():
    sol = Codethuattoan.rungeKutta(1000, 1, 0)
    assert [sol.S, sol.I, sol.R] == [
        999.9989996253158,
        1.0009003371740595,
        0.00010003751011400939,
    ]
