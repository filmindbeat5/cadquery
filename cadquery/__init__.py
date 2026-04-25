"""CadQuery - A parametric 3D CAD scripting framework.

CadQuery is an intuitive, easy-to-use Python module for building parametric
3D CAD models. It uses OpenCASCADE Technology (OCCT) as its underlying
geometry kernel.

Example usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(1, 2, 3)
    cq.exporters.export(result, "box.step")

Note: This is a personal fork. See https://github.com/CadQuery/cadquery
for the upstream project.

Personal notes:
    - Primarily using this for hobby CNC and 3D printing projects.
    - Workplane("XY") is the most common starting point for flat parts.
    - Remember: exporters.export supports STEP, STL, SVG, DXF formats.
    - For 3D printing, STL export with tolerance=0.01 gives good results.
    - Use Assembly for multi-part models with constraints.
    - DEFAULT_SVG_OPTS: handy defaults for SVG export (laser cutting).
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

# Default tolerance used for STL exports in my projects (good balance of
# quality vs. file size for FDM 3D printing).
DEFAULT_STL_TOLERANCE = 0.01

# Default SVG export options for laser cutting projects.
# projectionDir points straight down so the top face is shown.
DEFAULT_SVG_OPTS = {
    "projectionDir": (0, 0, -1),
    "showAxes": False,
    "strokeWidth": 0.25,
}

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
    # Personal defaults
    "DEFAULT_STL_TOLERANCE",
    "DEFAULT_SVG_OPTS",
]
