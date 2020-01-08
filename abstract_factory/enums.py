from enum import Enum


class FactoryEnum(Enum):
    MAC = 'Mac OS'
    WIN = 'Windows'
    GNOME = 'Gnome'


class GUIElementEnum(Enum):
    BUTTON = 'Button'
    INPUT = 'Input Field'
