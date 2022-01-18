import functools
import subprocess

subprocess_call = functools.partial(subprocess.call, stdout=subprocess.DEVNULL)

subprocess_call(["git", "init"])
subprocess_call(["git", "add", "*"])
subprocess_call(["git", "commit", "-m", "Initial commit"])
