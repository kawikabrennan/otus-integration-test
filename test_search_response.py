import unittest
from helpers import get_json_object
from jsonschema import validate
from schemas import build_assessment_search_response_schema
from schema_definitions import ASSESSMENT


class AssessmentSearchResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.response_json = get_json_object(
            "fixtures/search_response.json")

    def test_json_data_validation(self):
        """Verify JSON data against a schema"""
        schema = build_assessment_search_response_schema()
        validate(instance=self.response_json, schema=schema)

    def test_json_assessment_id_202089(self):
        """Validate all fields for assessment with matching id"""
        validate_test_id = []

        for assessment in self.response_json["data"]["AssessmentSearch"]:
            if assessment["assessment_id"] == 202089:
                validate_test_id.append(assessment)
                validate(instance=assessment, schema=ASSESSMENT)

        self.assertEqual(len(validate_test_id), 1)
