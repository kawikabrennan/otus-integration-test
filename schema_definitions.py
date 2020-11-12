ASSESSMENT = {
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
}

CLASSES = {
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
}

STUDENT = {
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
}
