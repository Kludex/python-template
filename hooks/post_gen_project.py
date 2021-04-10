import shutil


def remove_docs():
    shutil.rmtree("docs")


def main():
    if "{{ cookiecutter.add_docs }}" == "False":
        remove_docs()


if __name__ == "__main__":
    main()
