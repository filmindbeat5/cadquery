"""CadQuery - A parametric 3D CAD scripting framework.

CadQuery is an intuitive, easy-to-use Python module for building parametric
3D CAD models. It uses OpenCASCADE Technology (OCCT) as its underlying
geometry kernel.

Example usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(1, 2, 3)
    cq.exporters.export(result, "box.step")
"""

from .cq import (
    CQContext,
    CQObject,
    Workplane,
)
from .occ_impl.geom import (
    Vector,
    Matrix,
    Plane,
    Location,
)
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
)
from .occ_impl.assembly import (
    Assembly,
    Constraint,
)
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    RadiusNthSelector,
    CenterNthSelector,
    DirectionNthSelector,
    LengthNthSelector,
    AreaNthSelector,
    StringSyntaxSelector,
)
from . import exporters
from . import importers
from .cq_types import Real, VectorLike

__version__ = "2.4.0"

__all__ = [
    # Core classes
    "Workplane",
    "CQContext",
    "CQObject",
    # Geometry
    "Vector",
    "Matrix",
    "Plane",
    "Location",
    # Shapes
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    # Assembly
    "Assembly",
    "Constraint",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "DirectionMinMaxSelector",
    "RadiusNthSelector",
    "CenterNthSelector",
    "DirectionNthSelector",
    "LengthNthSelector",
    "AreaNthSelector",
    "StringSyntaxSelector",
    # Modules
    "exporters",
    "importers",
    # Types
    "Real",
    "VectorLike",
    # Version
    "__version__",
]
