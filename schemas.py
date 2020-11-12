def build_student_class_schema(target_json: dict) -> dict:
    schema = {
        "definitions": {
            "student": {
                "type": "object",
                "properties": {
                        "first": {"type": "string"},
                        "last": {"type": "string"},
                        "email": {"type": "string"},
                        "studentClasses": {
                            "type": "array",
                            "items": {"$ref": "#/definitions/studentClasses"}
                        }
                },
                "required": ["first", "last", "email", "studentClasses"],
                "additionalProperties": False,
            },
            "studentClasses": {
                "type": "object",
                "properties": {
                        "id": {"type": "number", "multipleOf": 1},
                        "grade": {
                            "type": "number",
                            "multipleOf": 0.5,
                            "minimum": 1,
                            "maximum": 4,
                        }
                },
                "required": ["id", "grade"],
                "additionalProperties": False,
            },
        },
        "type": "object",
        "properties": {
            "students": {
                "type": "array",
                "items": {"$ref": "#/definitions/student"}
            },
            "classes": {
                "type": "object",
                "properties": {
                    "1": {"type": "string"},
                    "2": {"type": "string"},
                    "3": {"type": "string"},
                    "4": {"type": "string"},
                    "5": {"type": "string"},
                    "6": {"type": "string"},
                    "7": {"type": "string"},
                    "8": {"type": "string"},
                },
                "required": ["1", "2", "3", "4", "5", "6", "7", "8"],
                "additionalProperties": False,
            }
        },
        "required": ["students", "classes"],
        "additionalProperties": False,
    }

    return schema


def build_assessment_search_response_schema(target_json: dict) -> dict:
    schema = {
        "definitions": {
            "assessment": {
                "type": "object",
                "properties": {
                        "assessment_id": {"type": "number", "multiple": 1},
                        "assessment_title": {"type": "string"},
                        "assessment_type": {"type": "number", "multiple": 1},
                        "district_id": {"type": "number", "multiple": 1},
                        "grading_scale_id": {"type": "number", "multiple": 1},
                        "__typename": {"const": "AssessmentSearch"}
                },
                "required": [
                    "assessment_id",
                    "assessment_title",
                    "assessment_type",
                    "district_id",
                    "grading_scale_id",
                    "__typename"
                ],
                "additionalProperties": False,
            },
        },
        "type": "object",
        "properties": {
            "data": {
                "type": "object",
                "properties": {
                    "AssessmentSearch": {
                        "type": "array",
                        "items": {"$ref": "#/definitions/assessment"}
                    }
                }
            },
        }
    }

    return schema
