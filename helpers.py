import json


def get_json_object(file_path: str) -> dict:
    with open(file_path) as file:
        try:
            test_json = json.load(file)
        except json.decoder.JSONDecodeError:
            test_json = {}
    return test_json
