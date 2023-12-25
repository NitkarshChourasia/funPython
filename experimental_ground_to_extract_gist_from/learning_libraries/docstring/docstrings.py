# Learning to write docstrings.


from math import pi


def area_of_circle(radius):
    """Calculate the area of a circle given its radius.

    Parameters
    ----------
    radius : float
        The radius of the circle in meters.

    Returns
    -------
    float
        The area of the circle in square meters.

    Raises
    ------
    ValueError
        If the radius is negative or zero.

    Examples
    --------
    >>> area_of_circle(1)
    3.141592653589793
    >>> area_of_circle(2.5)
    19.634954084936208
    >>> area_of_circle(-1)
    Traceback (most recent call last):
      ...
    ValueError: Radius must be positive.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    return pi * radius**2
