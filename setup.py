from setuptools import setup, find_packages


setup(
    name='jpxtime3',
    version='0.0.1',
    packages=find_packages(),
    package_data = {'': ['*pickle4']},
    description='Japan Exchange Delivatives(Index) trading schedule and trading hours',
    author='driller',
    classfiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=['python-dateutil']
)
