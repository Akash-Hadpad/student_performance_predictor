from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
    name='student_performance_predictor',
    version='0.0.1',
    author='Akash',
    author_email='akashdhsrnm@gmail.com',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'seaborn', 'matplotlib'],
)