import unittest
from helpers import get_json_object
from jsonschema import validate
from schemas import build_assessment_search_response_schema


class AssessmentSearchResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.response_json = get_json_object(
            "fixtures/search_response.json")

    def test_json_data_validation(self):
        """Verify JSON data against a schema"""
        schema = build_assessment_search_response_schema(self.response_json)
        validate(instance=self.response_json, schema=schema)
