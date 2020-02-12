from setuptools import setup, find_packages
import re

package_name = 'condatest'

with open('README.md', mode='r') as f:
    long_descr = f.read()

with open("src/{}/__init__.py".format(package_name), "r", encoding="utf8") as f:
    ver = re.search(r"__version__ = \'(.*?)\'", f.read()).group(1)

setup(
    name=package_name,
    version=ver,

    package_dir={"": "src"},
    packages=find_packages(where="src"),

    url='',
    license='MIT',
    author='Markus Franke',
    author_email='test@test.de',

    description='A test on how to build a conda package',
    long_description=long_descr,
    long_description_content_type='text/markdown'
)
