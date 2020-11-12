from schema_definitions import ASSESSMENT, CLASSES, STUDENT


def build_student_class_schema(target_json: dict) -> dict:
    schema = {
        "definitions": {
            "student": STUDENT,
            "studentClasses": CLASSES
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
            "assessment": ASSESSMENT
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
