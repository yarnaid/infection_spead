import pytest
import Codethuattoan
import sys
import numpy as np


@pytest.mark.example1
def test_mode_rungeKutta():
    a = np.array([1000, 1, 0])
    sol = Codethuattoan.rungeKutta(a)
    assert [sol[0], sol[1], sol[2]] == [
        999.9989996253158,
        1.0009003371740595,
        0.00010003751011400939,
    ]
