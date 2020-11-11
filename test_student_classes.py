import unittest
import json


class StudentClassResponse(unittest.TestCase):
    def test_valid_json(self):
        valid = True
        with open("fixtures/students_classes.json") as file:
            try:
                json.load(file)
            except json.decoder.JSONDecodeError:
                valid = False
        self.assertTrue(valid)
