import unittest

from .factories import FactoryProducer
from .enums import FactoryEnum, GUIElementEnum


class AbstractFactoryTest(unittest.TestCase):

    def test_not_implemented_factory(self):
        self.assertRaises(
            NotImplementedError,
            FactoryProducer.get_factory,
            'NotExistingFactory'
        )


class MacFactoryTest(unittest.TestCase):

    def setUp(self):
        self.factory = FactoryProducer.get_factory(FactoryEnum.MAC)

    def test_not_implemented_element(self):
        self.assertRaises(
            NotImplementedError,
            self.factory.get_gui_element,
            'NotExistingGuiElement'
        )

    def test_button(self):
        self.assertEqual(
            self.factory.get_gui_element(GUIElementEnum.BUTTON).render(),
            'I am a MacButton'
        )

    def test_input(self):
        self.assertEqual(
            self.factory.get_gui_element(GUIElementEnum.INPUT).render(),
            'I am a MacInputField'
        )


class WinFactoryTest(unittest.TestCase):

    def setUp(self):
        self.factory = FactoryProducer.get_factory(FactoryEnum.WIN)

    def test_not_implemented_element(self):
        self.assertRaises(
            NotImplementedError,
            self.factory.get_gui_element,
            'NotExistingGuiElement'
        )

    def test_button(self):
        self.assertEqual(
            self.factory.get_gui_element(GUIElementEnum.BUTTON).render(),
            'I am a WinButton'
        )

    def test_input(self):
        self.assertEqual(
            self.factory.get_gui_element(GUIElementEnum.INPUT).render(),
            'I am a WinInputField'
        )


class GnomeFactoryTest(unittest.TestCase):

    def setUp(self):
        self.factory = FactoryProducer.get_factory(FactoryEnum.GNOME)

    def test_not_implemented_element(self):
        self.assertRaises(
            NotImplementedError,
            self.factory.get_gui_element,
            'NotExistingGuiElement'
        )

    def test_button(self):
        self.assertEqual(
            self.factory.get_gui_element(GUIElementEnum.BUTTON).render(),
            'I am a GnomeButton'
        )

    def test_input(self):
        self.assertEqual(
            self.factory.get_gui_element(GUIElementEnum.INPUT).render(),
            'I am a GnomeInputField'
        )


if __name__ == "__main__":
    unittest.main()
