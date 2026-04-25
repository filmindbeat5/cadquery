"""Geometry primitives and transformation utilities for CadQuery.

This module provides Vector, Matrix, and Plane classes that form the
geometric foundation for all CadQuery operations.
"""

import math
from typing import Optional, Sequence, Tuple, Union

from OCP.gp import (
    gp_Ax1,
    gp_Ax2,
    gp_Ax3,
    gp_Dir,
    gp_Pln,
    gp_Pnt,
    gp_Trsf,
    gp_Vec,
    gp_XYZ,
)


class Vector:
    """A 3D vector with common mathematical operations.

    Wraps OCC's gp_Vec for use in CadQuery's higher-level API.
    """

    def __init__(self, *args):
        """Create a Vector from various input formats.

        Accepts:
            - Vector(x, y, z)
            - Vector((x, y, z))
            - Vector(gp_Vec)
            - Vector(gp_Pnt)
            - Vector(gp_Dir)
            - Vector(gp_XYZ)
        """
        if len(args) == 3:
            self._v = gp_Vec(*[float(a) for a in args])
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, (list, tuple)) and len(arg) == 3:
                self._v = gp_Vec(*[float(a) for a in arg])
            elif isinstance(arg, gp_Vec):
                self._v = arg
            elif isinstance(arg, gp_Pnt):
                self._v = gp_Vec(arg.X(), arg.Y(), arg.Z())
            elif isinstance(arg, gp_Dir):
                self._v = gp_Vec(arg.X(), arg.Y(), arg.Z())
            elif isinstance(arg, gp_XYZ):
                # gp_XYZ is a common OCC type; handy to support directly
                self._v = gp_Vec(arg.X(), arg.Y(), arg.Z())
            else:
                raise TypeError(f"Cannot create Vector from {type(arg)}")
        else:
            raise TypeError("Vector requires 1 or 3 arguments")

    @property
    def x(self) -> float:
        return self._v.X()

    @property
    def y(self) -> float:
        return self._v.Y()

    @property
    def z(self) -> float:
        return self._v.Z()

    def Length(self) -> float:  # noqa: N802
        """Return the magnitude of this vector."""
        return self._v.Magnitude()

    def normalized(self) -> "Vector":
        """Return a unit vector in the same direction."""
        return Vector(self._v.Normalized())

    def dot(self, other: "Vector") -> float:
        """Compute the dot product with another vector."""
        return self._v.Dot(other._v)

    def cross(self, other: "Vector") -> "Vector":
        """Compute the cross product with another vector."""
        return Vector(self._v.Crossed(other._v))

    def add(self, other: "Vector") -> "Vector":
        """Return the sum of this vector and another."""
        return Vector(self._v.Added(other._v))

    def sub(self, other: "Vector") -> "Vector":
        """Return the difference of this vector and another."""
        return Vector(self._v.Subtracted(other._v))

    def multiply(self, scale: float) -> "Vector":
        """Return this vector scaled by a scalar."""
        return Vector(self._v.Multiplied(scale))

    def getAngle(self, other: "Vector") -> float:  # noqa: N802
        """Return the angle in radians between this vector and another."""
        return self._v.Angle(other._v)

    def toTuple(self) -> Tuple[float, float, float]:  # noqa: N
