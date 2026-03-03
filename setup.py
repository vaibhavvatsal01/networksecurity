from setuptools import find_packages,setup
from typing import List
def get_requirements()->list[str]:

    """ this func returns list of requirements """
    requirement_list:list[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read line from file
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                ##ignore miss lines and -e.
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_list               

setup(
    name="networksecurity",
    version="0.0.1",
    author="vaibhav vatsal",
    author_email="vaibhavvatsalpandey01@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)


