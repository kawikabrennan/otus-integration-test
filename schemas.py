def build_student_class_schema(target_json: dict) -> dict:
    # classes = build_classes_property(target_json)
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
                "additionalProperties": False,
            }
        },
        "additionalProperties": False,
    }

    return schema


def build_classes_property(target_json):
    default = {
        "1": {"type": "string"},
        "2": {"type": "string"},
        "3": {"type": "string"},
        "4": {"type": "string"},
        "5": {"type": "string"},
        "6": {"type": "string"},
        "7": {"type": "string"},
        # "8": {"type": "string"}
    }
    custom = {}

    try:
        for item in target_json["classes"]:
            print("hey")
            print(item)
            custom[item.key] = {"type": "string"}
    except:
        print("what")
        custom = default

    # print(custom)
    return custom
