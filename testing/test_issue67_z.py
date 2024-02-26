"Second part of pytest>=7 incompatibility repro case. See also: `test_issue67_a.py`"


def test_no_forky():
    """When ran after `test_issue67_a.py`, this test will explode because
    `test_issue67_a` module is still on stack"""
    pass
