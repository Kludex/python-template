"""Based on: https://dilililabs.com/zh/blog/2021/01/19/publishing-a-proprietary-python-package-on-pypi-using-poetry/
"""
import multiprocessing
from pathlib import Path
from typing import List

from setuptools import Distribution, Extension

from Cython.Build import cythonize
from Cython.Distutils.build_ext import new_build_ext as cython_build_ext

SOURCE_DIR = Path("{{ cookiecutter.package }}")
BUILD_DIR = Path("dist")


def get_extension_modules() -> List[Extension]:
    """Collect all .py files and construct Setuptools Extensions"""
    extension_modules: List[Extension] = []

    for py_file in SOURCE_DIR.rglob("*.py"):
        module_path = py_file.with_suffix("")
        module_path = str(module_path).replace("/", ".")
        extension_module = Extension(name=module_path, sources=[str(py_file)])
        extension_modules.append(extension_module)

    return extension_modules


def cythonize_helper(extension_modules: List[Extension]) -> List[Extension]:
    return cythonize(
        module_list=extension_modules,
        build_dir=BUILD_DIR,
        annotate=False,
        nthreads=multiprocessing.cpu_count() * 2,
        compiler_directives={"language_level": "3"},
        force=True,
    )


distribution = Distribution(
    {
        "ext_modules": cythonize_helper(get_extension_modules()),
        "cmdclass": {"build_ext": cython_build_ext},
    }
)

distribution.run_command("build_ext")
build_ext_cmd = distribution.get_command_obj("build_ext")
build_ext_cmd.copy_extensions_to_source()
