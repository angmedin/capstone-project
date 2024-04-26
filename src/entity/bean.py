import datetime
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


@dataclass
class Bean():
    id: int
    load_timestamp: datetime.datetime
    area: int
    perimeter: Decimal
    major_axis_length: Decimal
    minor_axis_length: Decimal
    aspect_ration: Decimal
    eccentricity: Decimal
    convex_area: int
    equiv_diameter: Decimal
    extent: Decimal
    solidity: Decimal
    roundness: Decimal
    compactness: Decimal
    shape_factor_1: Decimal
    shape_factor_2: Decimal
    shape_factor_3: Decimal
    shape_factor_4: Decimal
    clazz: str


class BeanProperties(str, Enum):
    id = 'id'
    load_timestamp = 'load_timestamp'
    area = 'area'
    perimeter = 'perimeter'
    major_axis_length = 'major_axis_length'
    minor_axis_length = 'minor_axis_length'
    aspect_ration = 'aspect_ration'
    eccentricity = 'eccentricity'
    convex_area = 'convex_area'
    equiv_diameter = 'equiv_diameter'
    extent = 'extent'
    solidity = 'solidity'
    roundness = 'roundness'
    compactness = 'compactness'
    shape_factor_1 = 'shape_factor_1'
    shape_factor_2 = 'shape_factor_2'
    shape_factor_3 = 'shape_factor_3'
    shape_factor_4 = 'shape_factor_4'
    clazz = 'class'
