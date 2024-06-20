from setuptools import setup, find_packages

setup(
    name='healthcare_accessibility',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Django',
        'djangorestframework',
        'django-cors-headers',
    ],
    entry_points={
        'console_scripts': [
            'healthcare_accessibility=backend.manage:main',
        ],
    },
)
