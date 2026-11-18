from validator import validate

GOOD = (
    '{"summary": "Kickoff with Sam and Leila.", "decisions": [], '
    '"actions": [{"task": "Send RFP template", "owner": "Leila", "due_date": "not stated"}], '
    '"risks": [], "open_questions": [], "flags": []}'
)


def test_good_output_passes():
    assert validate(GOOD) == []


def test_invalid_json_is_rejected():
    assert validate("Meeting Summary: Kickoff") == ["not valid JSON"]


def test_missing_key_is_rejected():
    assert any("missing keys" in p for p in validate('{"summary": ""}'))
