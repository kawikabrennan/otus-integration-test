import unittest
from helpers import get_json_object
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from schemas import ASSESSMENT_SEARCH_RESPONSE_SCHEMA
from schema_definitions import ASSESSMENT


class AssessmentSearchResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.response_json = get_json_object(
            "fixtures/search_response.json")

    def test_json_data_validation(self):
        """Verify JSON data against a schema"""
        schema = ASSESSMENT_SEARCH_RESPONSE_SCHEMA
        validate(instance=self.response_json, schema=schema)

    def test_json_assessment_id_202089(self):
        """Validate all fields for assessment with matching id"""
        validate_test_id = []

        for assessment in self.response_json["data"]["AssessmentSearch"]:
            if assessment["assessment_id"] == 202089:
                validate_test_id.append(assessment)
                validate(instance=assessment, schema=ASSESSMENT)

        self.assertEqual(len(validate_test_id), 1)


class RainyDaySearchResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.response_json = get_json_object(
            "fixtures/search_response.json")

    def test_json_assessment_title_length_restriction(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to have smaller title length.
        """
        error = False

        schema = ASSESSMENT_SEARCH_RESPONSE_SCHEMA
        schema["definitions"]["assessment"]["properties"]["assessment_title"] = {
            "type": "string", "maxLength": 10
        }
        try:
            validate(instance=self.response_json, schema=schema)
        except ValidationError:
            error = True

        self.assertTrue(error)

    def test_json_assessment_type_change(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to have different type.
        """
        error = False

        schema = ASSESSMENT_SEARCH_RESPONSE_SCHEMA
        schema["definitions"]["assessment"]["properties"]["assessment_type"] = {
            "type": "string"
        }
        try:
            validate(instance=self.response_json, schema=schema)
        except ValidationError:
            error = True

        self.assertTrue(error)
