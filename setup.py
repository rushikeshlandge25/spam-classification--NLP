from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    
    with open(file_path) as file_obj:
        for req in file_obj.readlines():
            req = req.strip()        
            if req:                  
                requirements.append(req)
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)  # Remove '-e .'
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Rushikesh",
    author_email="rushirlandge@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)