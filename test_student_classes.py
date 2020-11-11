import unittest
import json
from jsonschema import validate
from schemas import build_student_class_schema


def get_json_object(file_path: str) -> dict:
    with open(file_path) as file:
        try:
            test_json = json.load(file)
        except json.decoder.JSONDecodeError:
            test_json = {}
    return test_json


class StudentClassResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.student_json = get_json_object(
            "fixtures/students_classes.json")

    def test_json_schema(self):
        schema = build_student_class_schema(self.student_json)
        validate(instance=self.student_json, schema=schema)
