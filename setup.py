from setuptools import setup, find_packages
import os


project_dir = os.path.dirname(__file__)

with open(
        os.path.join(project_dir, 'README.md'),
        encoding='utf8'
) as readme:
    long_description = readme.read()

setup(
    name='pre-commit-hooks',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    author='Yan Sokovnich',
    author_email='x6@live.ru',
    url='https://github.com/sokovnich/pre-commit-hooks',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'pre-commit-inject-issue-name = pre_commit_hooks.inject_issue_name:main',
        ],
    }
)
