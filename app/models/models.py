from dataclasses import dataclass


@dataclass
class Sport:
    key: str
    group: str
    title: str
    description: str
    active: bool
    has_outrights: bool
