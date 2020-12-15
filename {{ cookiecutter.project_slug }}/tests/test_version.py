import {{ cookiecutter.package }}

def test_version():
    assert {{ cookiecutter.package}}.__version__ == "0.1.0"
