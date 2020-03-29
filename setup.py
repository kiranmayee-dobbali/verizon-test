

from os import path

from setuptools import setup, find_packages


HERE = path.abspath(path.dirname(__file__))


with open('README.md', encoding='utf-8') as f:
    readme = f.read()

about = {}
with open(path.join(HERE, 'verizon', '__version__.py'), encoding='utf-8') as f:
    exec(f.read(), about)  # pylint: disable=exec-used


PACKAGES = ['verizon']


# Project Metadata

AUTHOR = 'SPIDER MAN'
AUTHOR_EMAIL = 'spiderman@spiderverse.com'

PYTHON_REQUIRES = '>=3.8'


setup(
    # minimum requirements
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    packages=find_packages(exclude=['test*']),

    author=AUTHOR,
    author_email=AUTHOR_EMAIL,

    python_requires=PYTHON_REQUIRES,


    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
)
