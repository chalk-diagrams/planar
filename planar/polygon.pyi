import planar
from _typeshed import Incomplete
from planar.util import assert_unorderable as assert_unorderable, cached_property as cached_property, cos_sin_deg as cos_sin_deg

class Polygon(planar.Seq2):
    def __init__(self, vertices, is_convex: Incomplete | None = ..., is_simple: Incomplete | None = ...) -> None: ...
    @classmethod
    def regular(cls, vertex_count, radius, center=..., angle: int = ...): ...
    @classmethod
    def star(cls, peak_count, radius1, radius2, center=..., angle: int = ...): ...
    @classmethod
    def from_points(cls, points): ...
    @property
    def bounding_box(self): ...
    @property
    def is_convex(self): ...
    @property
    def is_convex_known(self): ...
    @property
    def is_simple(self): ...
    @property
    def is_simple_known(self): ...
    @property
    def centroid(self): ...
    @property
    def is_centroid_known(self): ...
    def __setitem__(self, index, vert) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __imul__(self, other): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def contains_point(self, point): ...
    def tangents_to_point(self, point): ...
    @classmethod
    def convex_hull(cls, points): ...
