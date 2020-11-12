import unittest
from helpers import get_json_object
from jsonschema import validate
from schemas import STUDENT_CLASS_SCHEMA


class StudentClassResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.student_json = get_json_object(
            "fixtures/students_classes.json")

    def test_json_data_validation(self):
        """Verify JSON data against a schema"""
        schema = STUDENT_CLASS_SCHEMA
        validate(instance=self.student_json, schema=schema)
