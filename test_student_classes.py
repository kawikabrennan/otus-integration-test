import unittest
from helpers import get_json_object
from jsonschema import validate
from schemas import build_student_class_schema


class StudentClassResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.student_json = get_json_object(
            "fixtures/students_classes.json")

    def test_json_data_validation(self):
        """Verify JSON data against a schema"""
        schema = build_student_class_schema()
        validate(instance=self.student_json, schema=schema)
