
"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['numpy',
                'Pillow',
                'scikit-image',
                'scipy',
                'opencv-python',
                'fire',
                'matplotlib'
            ]

setup(
    author="Ryan Sudhakaran",
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A CLI tool for extracting sprites from spritesheets!",
    entry_points={
        'console_scripts': [
            'exsprite=exsprite.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    include_package_data=True,
    keywords='exsprite',
    name='exsprite',
    packages=find_packages(include=['exsprite', 'exsprite.*']),
    url='https://github.com/rysuds/exsprite',
    version='0.1.0',
    zip_safe=False,
)