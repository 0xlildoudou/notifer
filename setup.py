from setuptools import setup, find_packages

setup(
    name='notifer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'notify2',
    ],
    entry_points={
        'console_scripts': [
            'notifer=notifer.notifer:main',
        ],
    },
    package_data={'': ['assets/*']},
    python_requires='>=3.10'
)
