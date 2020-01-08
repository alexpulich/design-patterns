import json

from abc import ABC, abstractmethod
from enum import Enum


class ListConverterEnum(Enum):
    CSVConverter = 'CSVConverter'
    JSONConverter = 'JSONConverter'


class ListConverter(ABC):
    @abstractmethod
    def convert_list(self):
        pass


class CSVListConverter(ListConverter):

    def convert_list(self, list_):
        # dummy conversion for the sake of simplicity
        return ';'.join((str(item) for item in list_))


class JSONListConverter(ListConverter):

    def convert_list(self, list_):
        return json.dumps(list_)


class ListConverterFactory:
    CONDITION = {
        ListConverterEnum.CSVConverter: CSVListConverter,
        ListConverterEnum.JSONConverter: JSONListConverter
    }

    @staticmethod
    def get_converter(converter_type):
        try:
            return ListConverterFactory.CONDITION[converter_type]()
        except KeyError:
            raise NotImplementedError(f'{converter_type} is not implemented')
