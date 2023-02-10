from swe_as_code.lib.doit import doit


def test_doit() -> None:
    assert doit(2) == 4
