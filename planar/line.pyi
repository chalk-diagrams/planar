from _typeshed import Incomplete

class _LinearGeometry:
    @property
    def direction(self): ...
    @direction.setter
    def direction(self, value) -> None: ...
    @property
    def normal(self): ...
    @normal.setter
    def normal(self, value) -> None: ...

class Line(_LinearGeometry):
    direction: Incomplete
    offset: Incomplete
    def __init__(self, point, direction) -> None: ...
    @classmethod
    def from_points(cls, points): ...
    @classmethod
    def from_normal(cls, normal, offset): ...
    @property
    def points(self): ...
    def distance_to(self, point): ...
    def point_left(self, point): ...
    def point_right(self, point): ...
    def contains_point(self, point): ...
    def parallel(self, point): ...
    def perpendicular(self, point): ...
    def project(self, point): ...
    def reflect(self, point): ...
    def __imul__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def almost_equals(self, other): ...

class Ray(_LinearGeometry):
    direction: Incomplete
    def __init__(self, anchor, direction) -> None: ...
    @classmethod
    def from_points(cls, points): ...
    @property
    def points(self): ...
    @property
    def anchor(self): ...
    @anchor.setter
    def anchor(self, value) -> None: ...
    start: Incomplete
    @property
    def line(self): ...
    def distance_to(self, point): ...
    def contains_point(self, point): ...
    def point_behind(self, point): ...
    def point_left(self, point): ...
    def point_right(self, point): ...
    def project(self, point): ...
    def __imul__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def almost_equals(self, other): ...

class LineSegment(_LinearGeometry):
    def __init__(self, anchor, vector) -> None: ...
    @classmethod
    def from_points(cls, points): ...
    @classmethod
    def from_normal(cls, normal, offset, start_distance, end_distance): ...
    length: float
    @property
    def points(self): ...
    @property
    def anchor(self): ...
    @anchor.setter
    def anchor(self, value) -> None: ...
    start: Incomplete
    @property
    def vector(self): ...
    direction: Incomplete
    @vector.setter
    def vector(self, value) -> None: ...
    @property
    def end(self): ...
    @end.setter
    def end(self, value) -> None: ...
    @property
    def mid(self): ...
    @property
    def line(self): ...
    def distance_to(self, point): ...
    def contains_point(self, point): ...
    def point_ahead(self, point): ...
    def point_behind(self, point): ...
    def point_left(self, point): ...
    def point_right(self, point): ...
    def project(self, point): ...
    def __imul__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def almost_equals(self, other): ...
