from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the given file.
    It removes '-e .' if present and strips extra spaces or newlines from each entry.
    '''
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            # Clean up the list by stripping spaces and newlines
            requirements = [req.strip() for req in requirements if req.strip()]
            
            # Remove '-e .' if present in the list
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Nikita',
    author_email='nikitap02022002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

