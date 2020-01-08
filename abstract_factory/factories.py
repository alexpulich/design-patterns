from abc import ABC, abstractmethod

from .abstracts import AbstractFactory
from .enums import FactoryEnum, GUIElementEnum
from .gui import GnomeButton, GnomeInputField, MacButton, MacInputField, WinButton, WinInputField


class MacFactory(AbstractFactory):
    CONDITION = {
        GUIElementEnum.BUTTON: MacButton,
        GUIElementEnum.INPUT: MacInputField
    }

    @staticmethod
    def get_gui_element(element_type):
        try:
            return MacFactory.CONDITION[element_type]()
        except KeyError:
            raise NotImplementedError(f'{element_type} is not implemented')


class WinFactory(AbstractFactory):
    CONDITION = {
        GUIElementEnum.BUTTON: WinButton,
        GUIElementEnum.INPUT: WinInputField
    }

    @staticmethod
    def get_gui_element(element_type):
        try:
            return WinFactory.CONDITION[element_type]()
        except KeyError:
            raise NotImplementedError(f'{element_type} is not implemented')


class GnomeFactory(AbstractFactory):
    CONDITION = {
        GUIElementEnum.BUTTON: GnomeButton,
        GUIElementEnum.INPUT: GnomeInputField
    }

    @staticmethod
    def get_gui_element(element_type):
        try:
            return GnomeFactory.CONDITION[element_type]()
        except KeyError:
            raise NotImplementedError(f'{element_type} is not implemented')


class FactoryProducer:
    CONDITION = {
        FactoryEnum.GNOME: GnomeFactory,
        FactoryEnum.MAC: MacFactory,
        FactoryEnum.WIN: WinFactory
    }

    @staticmethod
    def get_factory(factory_type):
        try:
            return FactoryProducer.CONDITION[factory_type]
        except KeyError:
            raise NotImplementedError(f'{factory_type} is not implemented')
