"""Minimal repro case for https://github.com/pytest-dev/pytest-forked/issues/67.
See also: `test_issue67_z.py`"""

import pytest


def test_asetup_for_failure():
    "Non-forked test to get current module onto SetupState"
    pass


@pytest.mark.forked
def test_yyy():
    """
    Forked test as last test in the module.

    This way, teardown phase of previous test does not remove `test_issue67_a` module
    from the stack, and forked setups/teardowns do not leave the containment of the forked
    process.
    """
    pass


# Uncomment me to make tests pass O_-
# def test_zcleanup():
#     """As long as the last teardown of the module is ran in-process, stack should
#     stay valid for next module"""
#     pass
