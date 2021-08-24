import pytest
import Codethuattoan
import sys
import numpy as np


def test_mode_dS_dt():
    assert Codethuattoan.dS_dt(1000, 1) == -1


def test_mode_dI_dt():
    assert Codethuattoan.dI_dt(1, 1000) == 0.9


def test_mode_dR_dt():
    assert Codethuattoan.dR_dt(1) == 0.1


def test_mode_rungeKutta():
    a = np.array([1000, 1, 0])
    sol = Codethuattoan.rungeKutta(a)

    assert [sol[0], sol[1], sol[2]] == [
        999.9989996253158,
        1.0009003371740595,
        0.00010003751011400939,
    ]
