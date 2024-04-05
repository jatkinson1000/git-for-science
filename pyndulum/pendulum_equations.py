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

def get_l(period: float) -> float:
    return np.sqrt(9.81/period)*1.0/(2.0*np.pi)

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
