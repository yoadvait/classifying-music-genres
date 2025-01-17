from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

    return requirements

setup(
    name='MusicGenreClassification',
    version='0.1',
    author='YoAdvait',
    author_email='advait.iitd@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='Using Deep Learning Techniques to Classify Music Genres'
)