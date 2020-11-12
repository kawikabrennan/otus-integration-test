import unittest
import copy
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

    def setUp(self):
        self.schema = copy.deepcopy(ASSESSMENT_SEARCH_RESPONSE_SCHEMA)

    def result_validator(self, altered_schema: dict):
        error = False

        try:
            validate(instance=self.response_json, schema=altered_schema)
        except ValidationError:
            error = True

        self.assertTrue(error)

    def test_json_assessment_title_length_restriction(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to have smaller title length.
        """
        self.schema["definitions"]["assessment"]["properties"]["assessment_title"] = {
            "type": "string", "maxLength": 10
        }
        self.result_validator(self.schema)

    def test_json_assessment_title_regex(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to match a pattern.
        """
        self.schema["definitions"]["assessment"]["properties"]["assessment_title"] = {
            "type": "string", "pattern": "^[a-zA-Z]+$"
        }
        self.result_validator(self.schema)

    def test_json_assessment_type_change(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to have different type.
        """
        self.schema["definitions"]["assessment"]["properties"]["assessment_type"] = {
            "type": "string"
        }
        self.result_validator(self.schema)

    def test_json_assessment_type_range(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to be out of range.
        """
        self.schema["definitions"]["assessment"]["properties"]["assessment_type"] = {
            "type": "number", "maximum": 1
        }
        self.result_validator(self.schema)

    def test_json_district_id_type(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to be a string.
        """
        self.schema["definitions"]["assessment"]["properties"]["district_id"] = {
            "type": "string"
        }
        self.result_validator(self.schema)

    def test_json_district_id_maximum(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to be a maxium of 1.
        """
        self.schema["definitions"]["assessment"]["properties"]["district_id"] = {
            "type": "number", "maximum": 900
        }
        self.result_validator(self.schema)
