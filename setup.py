from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name="wbreakpoint",
    version="1.0",
    description="Project Description",
    packages=find_packages(),
    install_requires=requirements,
    test_suite="tests",
    zip_safe=False,
)
