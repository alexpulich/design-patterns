from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class InputField(ABC):
    @abstractmethod
    def render(self):
        pass


class AbstractFactory(ABC):
    @abstractmethod
    def get_gui_element(self, element_type):
        pass
