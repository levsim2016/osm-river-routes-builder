from setuptools import setup

import graph_builder

setup(
    name='rgbuilder',
    version=graph_builder.__version__,
    author='Lev Simionenko',
    author_email='lev.simionenko@gmail.com',
    entry_points={
        'console_scripts': [
            'rgbuilder = graph_builder.app:run'
        ]
    }
)
