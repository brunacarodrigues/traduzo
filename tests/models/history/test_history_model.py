import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    json_list = HistoryModel.list_as_json()
    tests = json.loads(json_list)

    assert len(tests) == 2
    assert tests[0]["text_to_translate"] == 'Hello, I like videogame'
    assert tests[0]["translate_from"] == 'en'
    assert tests[0]["translate_to"] == 'pt'
