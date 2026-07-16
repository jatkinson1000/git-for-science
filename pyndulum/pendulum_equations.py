"""Module implementing pendulum equations."""

import numpy as np


def get_period(len: float) -> float:
    """
    Calculate the period of a pendulum.

    Parameters
    ----------
    len : float
        length of the pendulum [m]

    Returns
    -------
    float
        period [s] for a swing of the pendulum
    """
    return 2.0 * np.pi * np.sqrt(len / 9.81)

def get_length(period: float) -> float:
    """
    Calculate the length of a pendulum from its period. Yu 2026-07-16 ICCS

    Parameters
    ----------
    period : float
        period of the pendulum [s]

    Returns
    -------
    float
        length of the pendulum [m]
    """
    return 9.81 * (period / (2.0 * np.pi))**2

def max_height(len: float, theta: float) -> float:
    """
    Calculate the maximum height reached by a pendulum.

    Parameters
    ----------
    len : float
        length of the pendulum [m]
    theta : float
        maximum angle of displacment of the pendulum [radians]

    Returns
    -------
    float
        maximum vertical height [m] of the pendulum
    """
    return len * np.cos(theta)


def max_speed(len: float, theta: float) -> float:
    """
    Calculate the maximum speed of a pendulum.

    Parameters
    ----------
    len : float
        length of the pendulum [m]
    theta : float
        maximum angle of displacment of the pendulum [radians]

    Returns
    -------
    float
        maximum speed [m/s] of the pendulum
    """
    return np.sqrt(2.0 * 9.81 * max_height(len, theta))


def check_small_angle(theta: float) -> bool:
    """
    Check small angle approximation is valid.

    Parameters
    ----------
    theta : float
        maximum angle of displacment of the pendulum [radians]

    Returns
    -------
    bool
        is the small angle approximation valid for the input theta?
    """
    if theta <= np.pi / 1800.0:
        return True
    return False


def bpm(len: float) -> float:
    """
    Calculate pendulum frequency in beats per minute.

    Parameters
    ----------
    len : float
        length of the pendulum [m]

    Returns
    -------
    float
        pendulum frequency in beats per minute [1 / min]
    """
    return 60.0 / get_period(len)
