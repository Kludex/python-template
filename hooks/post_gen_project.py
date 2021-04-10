import os
import shutil


def remove_docs():
    shutil.rmtree("docs")
    os.remove(".github/workflows/deploy-docs.yml")


def remove_cython():
    os.remove("build.py")


def main():
    if "{{ cookiecutter.add_docs }}" == "False":
        remove_docs()

    if "{{ cookiecutter.add_cython }}" == "False":
        remove_cython()


if __name__ == "__main__":
    main()
