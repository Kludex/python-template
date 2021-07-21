import os
import shutil
import subprocess


def remove_docs():
    shutil.rmtree("docs")
    os.remove(".github/workflows/deploy-docs.yml")


def git_init():
    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "🎉 First commit"])


def github_init():
    subprocess.call(
        [
            "gh",
            "repo",
            "create",
            "{{ cookiecutter.project_slug }}",
            "--public",
            "--description",
            "{{ cookiecutter.description }}",
            "--confirm",
        ]
    )
    subprocess.call("git", "push", "origin", "main")


def main():
    if "{{ cookiecutter.add_docs }}" == "False":
        remove_docs()

    git_init()
    github_init()


if __name__ == "__main__":
    main()
