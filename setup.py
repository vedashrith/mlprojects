from setuptools import find_packages, setup
from typing import List

HYPHE_E_DOT =  '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this func return the list of req
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHE_E_DOT in requirements:
            requirements.remove(HYPHE_E_DOT)

setup(
    name = 'mlprojects',
    version = '0.0.1',
    author = 'Vedh',
    author_email = 'vedashrithgoud@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)