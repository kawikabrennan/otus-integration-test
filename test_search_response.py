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

    def test_json_assessment_title_length_restriction(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to have smaller title length.
        """
        error = False

        # schema = copy.deepcopy(ASSESSMENT_SEARCH_RESPONSE_SCHEMA)
        self.schema["definitions"]["assessment"]["properties"]["assessment_title"] = {
            "type": "string", "maxLength": 10
        }
        try:
            validate(instance=self.response_json, schema=self.schema)
        except ValidationError:
            error = True

        self.assertTrue(error)

    def test_json_assessment_type_change(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to have different type.
        """
        error = False

        # schema = ASSESSMENT_SEARCH_RESPONSE_SCHEMA
        self.schema["definitions"]["assessment"]["properties"]["assessment_type"] = {
            "type": "string"
        }
        try:
            validate(instance=self.response_json, schema=self.schema)
        except ValidationError:
            error = True

        self.assertTrue(error)

    def test_json_district_id_type(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to be a string.
        """
        error = False

        # schema = ASSESSMENT_SEARCH_RESPONSE_SCHEMA
        self.schema["definitions"]["assessment"]["properties"]["district_id"] = {
            "type": "string"
        }
        try:
            validate(instance=self.response_json, schema=self.schema)
        except ValidationError:
            error = True

        self.assertTrue(error)

    def test_json_district_id_maximum(self):
        """Altering schema to show edge case testing.
        Update custom schema to expect untouched response data to be a maxium of 1.
        """
        error = False

        self.schema["definitions"]["assessment"]["properties"]["district_id"] = {
            "type": "number", "maximum": 1
        }
        try:
            validate(instance=self.response_json, schema=self.schema)
        except ValidationError:
            error = True

        self.assertTrue(error)
