from setuptools import setup, find_packages
import os

# Get the absolute path of requirements.txt
req_path = os.path.join(os.path.dirname(__file__), "requirements.txt")

# Read requirements.txt safely
with open(req_path, "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="RealtimeSTT",
    version="0.1",
    packages=find_packages(where="RealtimeSTT"),
    package_dir={"": "RealtimeSTT"},
    install_requires=requirements,
)
