import unittest

from .factory import ListConverterEnum, ListConverterFactory


class ListPrinterFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = ListConverterFactory
        self.list_ = ['a', 'bc', 123, 'test', '12#?287#8']
        self.empty_list = []

    def test_not_implemented_printer(self):
        self.assertRaises(
            NotImplementedError,
            self.factory.get_converter,
            'SomeNotExistingConverter'
        )

    def test_csv_printer_not_empty(self):
        converter = self.factory.get_converter(ListConverterEnum.CSVConverter)
        self.assertEqual(
            converter.convert_list(self.list_),
            'a;bc;123;test;12#?287#8'
        )

    def test_csv_printer_empty(self):
        converter = self.factory.get_converter(ListConverterEnum.CSVConverter)
        self.assertEqual(
            converter.convert_list(self.empty_list),
            ''
        )

    def test_json_printer_not_empty(self):
        converter = self.factory.get_converter(ListConverterEnum.JSONConverter)
        self.assertEqual(
            converter.convert_list(self.list_),
            '["a", "bc", 123, "test", "12#?287#8"]'
        )

    def test_json_printer_empty(self):
        converter = self.factory.get_converter(ListConverterEnum.JSONConverter)
        self.assertEqual(
            converter.convert_list(self.empty_list),
            '[]'
        )


if __name__ == "__main__":
    unittest.main()
