from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function returs all the requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='EndToEndMLProject',
    version='0.0.1',
    author='Jitesh',
    author_email='jitesh.kumar05official@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)