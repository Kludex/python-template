import inspect

import {{ cookiecutter.package }}


def test_smoke():
    assert inspect.ismodule({{ cookiecutter.package }})
