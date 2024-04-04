from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements=[req.replace("\n", "") for req in requirements]

    return requirements

setup(
    name="ML_Project",
    version="3.12.2",
    author="Bansari",
    author_email="bansaripanseriya010@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
