import inspect

import {{ cookiecutter.package }}


def test_smoke() -> None:
    assert inspect.ismodule({{ cookiecutter.package }})
